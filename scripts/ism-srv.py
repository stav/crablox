import argparse
from typing import Generator
from datetime import datetime
from dateutil.relativedelta import relativedelta

import requests
from bs4 import BeautifulSoup, Tag


url = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/services/may/"


def banner(url: str) -> None:
    print(
        f"""\n
|{'-' * (len(url) + 2)}|
| {url} |
|{'-' * (len(url) + 2)}|
"""
    )


def get_month_urls(
    months: int, skip_current: bool = True
) -> Generator[str, None, None]:
    """Generate URLs for the specified number of months.

    Args:
        months: Number of months to generate URLs for
        skip_current: Whether to skip the current month (default: True)

    Yields:
        URL for each month in sequence
    """
    current_date = datetime.now()

    # If skipping current month, start from previous month
    start_offset = 1 if skip_current else 0

    for i in range(months):
        # Go back i months from current date, plus the start offset
        target_date = current_date - relativedelta(months=(i + start_offset))
        month_name = target_date.strftime("%B").lower()
        yield f"https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/services/{month_name}/"


def find_results_table(soup: BeautifulSoup) -> Tag:
    """Find the table containing the results at a glance.

    Args:
        soup: BeautifulSoup object containing the parsed HTML

    Returns:
        BeautifulSoup Tag element representing the table

    Raises:
        ValueError: If the H3 tag or table is not found
    """
    # Find the H3 tag with the specific text
    h3_tags = soup.find_all("h3")
    for tag in h3_tags:
        if "RESULTS AT A GLANCE" in tag.get_text():
            h3_tag = tag
            break
    else:
        raise ValueError("H3 tag with 'RESULTS AT A GLANCE' not found")

    # Find the table immediately after the H3 tag
    table = h3_tag.find_next("table")
    if not table:
        raise ValueError("Table following the H3 tag not found")

    return table  # type: ignore


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


def process_glance_table(soup: BeautifulSoup) -> None:
    """Process and output the rows from the results table.

    Args:
        soup: BeautifulSoup object containing the parsed HTML

    Raises:
        ValueError: If the table or its contents cannot be found
    """
    print("\n#### The Key Numbers:")
    table = find_results_table(soup)
    rows = table.find("tbody").find_all("tr")  # type: ignore
    for row in rows:
        header_text = "No header"  # Default value
        header = row.find("th")  # type: ignore
        if header:
            header_text = header.get_text(strip=True).replace("®", "")[:30]  # type: ignore
            header_text = f"**{header_text}**"
            header_text = header_text.ljust(34)
        cells = row.find_all(["td"], limit=5)  # type: ignore
        if len(cells) == 5:
            c = [cell.get_text(strip=True) for cell in cells]
            if c[0] != "N/A":
                print(f"- {header_text} <br> {c[0]} vs {c[1]} ({c[2]}) → {c[3]} {c[4]}")


def process_industry_heatmap(
    growing_industries: list[str], contracting_industries: list[str]
) -> None:
    """Process and output the industry performance heatmap section.

    Args:
        growing_industries: List of growing industries
        contracting_industries: List of contracting industries

    Returns:
        None
    """
    print("\n#### Industry Heatmap")
    print(
        """
<style>
.heatmap-table {
    border-collapse: collapse;
    width: auto;
    border: 1px solid var(--pico-muted-border-color);
}
.heatmap-table th {
    background-color: var(--pico-muted-color);
    color: var(--pico-primary-inverse);
}
.growing-cell {
    color: black;
    background-color: rgb(var(--growing-r), 255, 0);
}
.contracting-cell {
    color: black;
    background-color: rgb(255, var(--contracting-g), 0);
}
.heatmap-table tr:hover .growing-cell {
    filter: brightness(1.1);
}
.heatmap-table tr:hover .contracting-cell {
    filter: brightness(1.1);
}
.heatmap-table td {
    transition: border-color 0.2s ease;
}
.heatmap-table tr:hover td {
    border: 1px solid var(--pico-primary);
}
</style>
"""
    )
    print("<table class='heatmap-table'>")
    print("<tr><th>Industry</th><th>Movement</th></tr>")

    # Process growing industries
    max_growing_rank = len(growing_industries)
    for i, industry in enumerate(growing_industries):
        rank = max_growing_rank - i
        # Calculate red component for growing industries (255 to 0)
        growing_r = int(255 * (1 - (rank / 20)))
        print(
            f"<tr><td class='industry'>{industry}</td><td class='growing-cell' style='--growing-r: {growing_r}'>Grow {rank}</td></tr>"
        )

    # Process contracting industries in reverse order
    for i, industry in enumerate(reversed(contracting_industries)):
        rank = i + 1
        # Calculate green component for contracting industries (255 to 0)
        contracting_g = int(255 * (1 - (rank / 20)))
        print(
            f"<tr><td class='industry'>{industry}</td><td class='contracting-cell' style='--contracting-g: {contracting_g}'>Contract -{rank}</td></tr>"
        )

    print("</table>")


def process_industrys(soup: BeautifulSoup, heatmap_only: bool = False) -> None:
    """Process and output the industry performance heatmap section.

    Args:
        soup: BeautifulSoup object containing the parsed HTML

    Raises:
        ValueError: If the industry performance section cannot be found
    """
    p_tag = find_industry_paragraph(soup)
    text = p_tag.get_text(strip=True)
    growing_industries, contracting_industries = parse_industry_text(text)

    if not heatmap_only:
        print("\n### Industry Performance")
        if growing_industries:
            print("\n#### Growing Industries:")
            for industry in growing_industries:
                print(f"1. {industry}")

        if contracting_industries:
            print("\n#### Contracting Industries:")
            for industry in contracting_industries:
                print(f"1. {industry}")

    process_industry_heatmap(growing_industries, contracting_industries)


def scrape_ism_report(months: int = 1, skip_current: bool = True, heatmap_only: bool = False):
    for url in get_month_urls(months, skip_current):
        banner(url)
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        soup = BeautifulSoup(response.text, "html.parser")  # type: ignore
        if not heatmap_only:
            process_glance_table(soup)
        process_industrys(soup, heatmap_only)


def main():
    parser = argparse.ArgumentParser(
        description="Scrape ISM Services Report for a specified number of months"
    )
    parser.add_argument(
        "--months",
        "-m",
        type=int,
        default=1,
        help="Number of months to scrape (default: 1)",
    )
    parser.add_argument(
        "--include-current",
        "-c",
        action="store_true",
        help="Include the current month (default: skip current month)",
    )
    parser.add_argument(
        "--heatmap-only",
        "-o",
        action="store_true",
        help="Only show the industry heatmap (default: false)",
    )
    args = parser.parse_args()

    try:
        scrape_ism_report(args.months, not args.include_current, args.heatmap_only)
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    exit(main())
