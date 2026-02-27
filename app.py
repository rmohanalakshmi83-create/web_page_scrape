from flask import Flask
from utils import scrape_quotes

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Quotes Web Scraper</h2>
    <a href='/run'>Run Scraper</a>
    """

@app.route("/run")
def run_scraper():
    try:
        message = scrape_quotes()
        return message
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)