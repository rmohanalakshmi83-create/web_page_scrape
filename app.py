from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Quotes Web Scraper</h2>
    <a href='/run'>Run Scraper</a>
    """

@app.route("/run")
def run_scraper():
    import requests
    from bs4 import BeautifulSoup

    base_url = "http://quotes.toscrape.com/page/{}/"
    quotes = []

    for page in range(1, 6):  # Change 6 to scrape more pages
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for quote in soup.find_all("span", class_="text"):
            quotes.append(quote.text)

    return render_template("quotes.html", quotes=quotes)