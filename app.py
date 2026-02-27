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
    base_url = "http://quotes.toscrape.com"
    quotes = []
    page_url = "/page/1/"

    while page_url:
        response = requests.get(base_url + page_url)
        soup = BeautifulSoup(response.text, "html.parser")

        for quote in soup.find_all("span", class_="text"):
            quotes.append(quote.text)

        next_btn = soup.find("li", class_="next")
        if next_btn:
            page_url = next_btn.find("a")["href"]
        else:
            page_url = None

    return render_template("quotes.html", quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)