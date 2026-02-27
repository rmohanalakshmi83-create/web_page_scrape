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
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = []

    for quote in soup.find_all("span", class_="text"):
        quotes.append(quote.text)

    return render_template("quotes.html", quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)