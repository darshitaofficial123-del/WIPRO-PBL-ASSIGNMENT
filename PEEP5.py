import requests
from bs4 import BeautifulSoup

# Retrieve HTML
url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
r = requests.get(url)
html_text = r.text

# Parse HTML
soup = BeautifulSoup(html_text, "html.parser")

# Extract all text portions
texts = [t.strip() for t in soup.stripped_strings]

print(texts)
