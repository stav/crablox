import json
import argparse
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pathlib import Path
from typing import Generator, Dict

import requests
from bs4 import BeautifulSoup, Tag


def get_month_urls(
    months: int, skip_current: bool = True
) -> Generator[tuple[str, datetime], None, None]:
    """Generate URLs for the specified number of months.

    Args:
        months: Number of months to generate URLs for
        skip_current: Whether to skip the current month (default: True)

    Yields:
        Tuple of (URL, datetime) for each month in sequence
    """
    current_date = datetime.now()

    # If skipping current month, start from previous month
    start_offset = 1 if skip_current else 0

    for i in range(months):
        # Go back i months from current date, plus the start offset
        target_date = current_date - relativedelta(months=(i + start_offset))
        month_name = target_date.strftime("%B").lower()
        url = f"https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/services/{month_name}/"
        yield url, target_date


def find_industry_paragraph(soup: BeautifulSoup) -> Tag:
    """Find the paragraph containing industry performance information.

    Args:
        soup: BeautifulSoup object containing the parsed HTML

    Returns:
        BeautifulSoup Tag element representing the paragraph

    Raises:
        ValueError: If the H3 tag or paragraph is not found
    """
    # Find the H3 tag with the specific text
    h3_tags = soup.find_all("h3")
    for tag in h3_tags:
        if "INDUSTRY PERFORMANCE" in tag.get_text():
            h3_tag = tag
            break
    else:
        raise ValueError("H3 tag with 'INDUSTRY PERFORMANCE' not found")

    # Find the paragraph immediately after the H3 tag
    p_tag = h3_tag.find_next("p")
    if not p_tag:
        raise ValueError(
            "Paragraph following the industry performance H3 tag not found"
        )

    return p_tag  # type: ignore


def parse_industry_text(text: str) -> tuple[list[str], list[str]]:
    """Parse the industry performance text into lists of growing and contracting industries.

    Args:
        text: The raw text from the industry performance paragraph

    Returns:
        Tuple of (growing_industries, contracting_industries)
    """
    # Split the text into growing and contracting sections
    parts = text.split("listed in order — are:")
    if len(parts) != 3:  # We expect 3 parts: intro, growing list, contracting list
        return [], []

    def process_list(text: str):
        lines = text.split(";")
        for line in lines:
            line = line.strip()
            if line.startswith("and "):
                line = line.replace("and ", "", 1)
            if "." in line:
                line = line.split(".")[0]
            if line:
                yield line

    growing_industries = list(process_list(parts[1]))
    contracting_industries = list(process_list(parts[2]))

    return growing_industries, contracting_industries


def get_industry_data(soup: BeautifulSoup) -> Dict[str, int]:
    """Extract industry performance data from the page.

    Args:
        soup: BeautifulSoup object containing the parsed HTML

    Returns:
        Dictionary mapping industry names to their growth rank (positive for growing, negative for contracting)
    """
    p_tag = find_industry_paragraph(soup)
    text = p_tag.get_text(strip=True)
    growing_industries, contracting_industries = parse_industry_text(text)

    industry_data = {}

    # Process growing industries
    max_growing_rank = len(growing_industries)
    for i, industry in enumerate(growing_industries):
        rank = max_growing_rank - i
        industry_data[industry] = rank

    # Process contracting industries in reverse order
    for i, industry in enumerate(reversed(contracting_industries)):
        rank = -(i + 1)  # Negative rank for contracting industries
        industry_data[industry] = rank

    return industry_data


def load_existing_data(file_path: Path) -> Dict[str, Dict[str, int]]:
    """Load existing data from JSON file if it exists.

    Args:
        file_path: Path to the JSON file

    Returns:
        Dictionary containing existing data or empty dict if file doesn't exist
    """
    if file_path.exists():
        with file_path.open("r") as f:
            return json.load(f)
    return {}


def scrape_ism_heat_data(months: int, skip_current: bool, output_file: str):
    """Scrape ISM Services Report heatmap data for multiple months and save to JSON.

    Args:
        months: Number of months to scrape
        skip_current: Whether to skip the current month
        output_file: Path to save the JSON data
    """
    # Ensure data directory exists
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Load existing data
    heat_data = load_existing_data(output_path)
    print(f"Loaded {len(heat_data)} existing industries")

    # Track which months we're updating
    months_to_update = set()

    # First pass: collect all unique industries and track months to update
    for url, date in get_month_urls(months, skip_current):
        month_key = date.strftime("%Y-%m")
        months_to_update.add(month_key)
        print(f"Collecting industries from {date.strftime('%B %Y')}...")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        month_data = get_industry_data(soup)

        # Add any new industries to our main structure
        for industry in month_data:
            if industry not in heat_data:
                heat_data[industry] = {}

    # Second pass: update only the months we're scraping
    for url, date in get_month_urls(months, skip_current):
        print(f"Scraping data for {date.strftime('%B %Y')}...")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        month_data = get_industry_data(soup)

        # Update this month's data for each industry
        month_key = date.strftime("%Y-%m")
        for industry in heat_data:
            heat_data[industry][month_key] = month_data.get(
                industry, 0
            )  # Use 0 for missing data

    # Sort industries by their most recent month's performance
    def get_latest_value(industry_data):
        if not industry_data:
            return 0
        return list(industry_data.values())[-1]

    sorted_heat_data = dict(
        sorted(heat_data.items(), key=lambda x: get_latest_value(x[1]), reverse=True)
    )

    # Save to JSON file
    with output_path.open("w") as f:
        json.dump(sorted_heat_data, f, indent=2)

    print(f"\nUpdated data for months: {', '.join(sorted(months_to_update))}")
    print(f"Data saved to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Scrape ISM Services Report heatmap data for multiple months"
    )
    parser.add_argument(
        "--months",
        "-m",
        type=int,
        default=3,
        help="Number of months to scrape (default: 3)",
    )
    parser.add_argument(
        "--include-current",
        "-c",
        action="store_true",
        help="Include the current month (default: skip current month)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default="data/ism_heat_data.json",
        help="Output JSON file path (default: data/ism_heat_data.json)",
    )
    args = parser.parse_args()

    try:
        scrape_ism_heat_data(args.months, not args.include_current, args.output)
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
