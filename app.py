from flask import Flask, render_template
from utils import scrape_quotes
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Quotes Web Scraper</h2>
    <a href='/run'>Run Scraper</a>
    """

@app.route("/run")
def run_scraper():
    # Run scraper (saves CSV)
    scrape_quotes()

    # Read CSV to display data
    quotes = []
    with open("quotes.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            quotes.append(row[0])  # only quote text

    return render_template("quotes.html", quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)