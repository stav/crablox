import requests
from bs4 import BeautifulSoup

url = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/services/march/"


def scrape_ism_report():

    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for HTTP issues

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the H3 tag with the specific text
    # h3_tag = soup.find_all('h3', string=lambda text: text and "RESULTS AT A GLANCE" in text)
    h3_tags = soup.find_all("h3")
    for tag in h3_tags:
        if "RESULTS AT A GLANCE" in tag.get_text():
            h3_tag = tag
            break
    else:
        print("H3 tag with the specified text not found.")
        return

    # Find the table immediately after the H3 tag
    table = h3_tag.find_next("table")
    if not table:
        print("Table following the H3 tag not found.")
        return

    # Extract table rows and cells
    rows = table.find("tbody").find_all("tr")
    for row in rows:
        header = row.find("th")
        if header:
            header_text = header.get_text(strip=True).replace("®", "")[:30]
            header_text = f"**{header_text}**"
            header_text = header_text.ljust(34)
        cells = row.find_all(["td"], limit=5)
        if len(cells) == 5:
            c = [cell.get_text(strip=True) for cell in cells]
            if c[0] != "N/A":
                print(f"- {header_text} : {c[0]} vs {c[1]} ({c[2]}) → {c[3]} {c[4]}")


if __name__ == "__main__":
    scrape_ism_report()
