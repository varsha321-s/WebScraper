import time
import requests
from bs4 import BeautifulSoup
import csv
import json

url = "https://news.ycombinator.com/"

try:
    response = requests.get(url)
    time.sleep(2)
    response.raise_for_status()

except Exception as e:
    print("Error:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

data = []

keyword = input("Enter keyword to search (or press Enter for all): ").lower()

with open("headlines.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Headline", "URL"])

    for title in titles:

        link = title.find("a")

        headline = link.text
        news_url = link["href"]

        if keyword and keyword not in headline.lower():
            continue

        writer.writerow([headline, news_url])

        data.append({
            "headline": headline,
            "url": news_url
        })

with open("headlines.json", "w", encoding="utf-8") as json_file:

    json.dump(data, json_file, indent=4)

print("CSV and JSON files created successfully!")