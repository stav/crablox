import re
from pprint import pprint
from typing import List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

url = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/"


def extract_text_between_tags(soup, start_tag, end_tag):
    start_tag = soup.find(start_tag)
    if not start_tag:
        return {"error": "Start tag not found."}
    end_tag = start_tag.find(end_tag)
    if not end_tag:
        return {"error": "End tag not found."}


def extract_from_first_element(tags, text):
    # Find the h1 tag with the specific text
    for tag in tags:
        if text in tag.get_text():
            return tag, tag.get_text().strip()
    return None, f"Tag not found with text: '{text}'"


def scrape_ism_report_url():

    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for HTTP issues

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the H3 tag with the specific text
    # h3_tag = soup.find_all('h3', string=lambda text: text and "RESULTS AT A GLANCE" in text)
    h3_tags = soup.find_all("h3")
    for tag in h3_tags:
        if "Manufacturing PMI" in tag.get_text():
            h3_tag = tag
            break
    else:
        print("H3 tag with the specified text not found.")
        return

    # Find the paragraph immediately after the H3 tag
    p_tag = h3_tag.find_next("p")  # type: ignore
    if not p_tag:
        print("P following the H3 tag not found.")
        return

    # Extract the link from the p tag
    a_tag = p_tag.find("a")  # type: ignore
    if not a_tag:
        print("Link not found in the table.")
        return

    # Get the href attribute from the a tag
    link = a_tag.get("href")  # type: ignore
    if not link:
        print("No href attribute found in the link.")
        return

    if not isinstance(link, str):
        print("Invalid link type found.")
        return

    return urljoin(url, link)


def scrape_ism_report_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for HTTP issues

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the main tag
    main_tag = soup.find("main", id="main")  # type: ignore
    if not main_tag:
        return {"error": "Main tag not found."}

    # Extract the score
    score_tag, score_text = extract_from_first_element(
        main_tag.find_all("h1"), "Manufacturing PMI"  # type: ignore
    )
    score = "No score tag found."
    if score_tag:
        # Extract the float percentage using regex
        match = re.search(r"(\d+\.\d+)%", score_text)
        if match:
            score = match.group(1)
        else:
            score = "No float percentage found in the text."

    # Extract the title
    title_tag = score_tag.find_next("h1")  # type: ignore
    title_text = "No title tag found."
    month = "Unknown"
    year = "Unknown"
    if title_tag:
        title_text = title_tag.get_text().strip()
        # Extract month and year from title
        match = re.search(r"(\w+)\s+(\d{4})", title_text)
        if match:
            month = match.group(1)
            year = match.group(2)

    # Extract the next H3 tag with summary bullet points
    bullets_tag = title_tag.find_next("h3")  # type: ignore
    if bullets_tag:
        bullets: List[str] = [
            text.strip() for text in bullets_tag.stripped_strings if text.strip()
        ]
    else:
        bullets = []

    # Extract the Manufacturing at a glance header
    glance_tag, glance_text = extract_from_first_element(
        main_tag.find_all("h3"), "MANUFACTURING AT A GLANCE"  # type: ignore
    )
    # if glance_tag:

    # Find the table immediately after the H3 tag
    table = glance_tag.find_next("table")  # type: ignore
    if not table:
        print("Table following the H3 tag not found.")
        return

    # Extract table rows and cells
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
                print(f"- {header_text} : {c[0]} vs {c[1]} ({c[2]}) → {c[3]} {c[4]}")


    # Return the data
    return {
        "score_text": score_text.replace("®", ""),
        "score": score,
        "title": title_text.replace("®", ""),
        "month": month,
        "year": year,
        "bullets": bullets,
    }


def main():
    url = scrape_ism_report_url()
    if url:
        data = scrape_ism_report_data(url)
        pprint(data, width=100)
    else:
        print(f"No URL found: ({url}).")


if __name__ == "__main__":
    main()
