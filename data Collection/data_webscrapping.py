import requests
from bs4 import BeautifulSoup

html = requests.get("https://quotes.toscrape.com/").text
soup = BeautifulSoup(html, "html.parser")

quotes = [q.text.strip() for q in soup.select(".text")]
print(quotes)
