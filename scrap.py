import requests
from bs4 import BeautifulSoup
import pandas as pd

quotes = []
authors = []
tags = []

for page in range(1, 11):

    url = f"https://quotes.toscrape.com/page/{page}/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quote_blocks = soup.find_all("div", class_="quote")

    for quote in quote_blocks:
        quotes.append(quote.find("span", class_="text").text)
        authors.append(quote.find("small", class_="author").text)

        tag_list = [tag.text for tag in quote.find_all("a", class_="tag")]
        tags.append(", ".join(tag_list))

df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors,
    "Tags": tags
})

# CSV file save karna
df.to_csv("quotes_dataset.csv", index=False, encoding="utf-8")

# Output
print("Dataset Saved!")
print("Total Records:", len(df))
print("\nFirst 10 Records:\n")
print(df.head(10))