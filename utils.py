import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    base_url = "https://quotes.toscrape.com/"
    page_url = base_url
    all_data = []
    seen = set()

    while page_url:
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        for q in quotes:
            text = q.find("span", class_="text").get_text().strip()
            author = q.find("small", class_="author").get_text().strip()
            tags = [t.get_text().strip() for t in q.find_all("a", class_="tag")]

            if text not in seen:
                seen.add(text)
                all_data.append([text, author, ", ".join(tags)])

        next_btn = soup.find("li", class_="next")
        if next_btn:
            page_url = base_url + next_btn.find("a")["href"]
        else:
            page_url = None

    with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Quote", "Author", "Tags"])
        writer.writerows(all_data)

    return "Scraping completed successfully!"