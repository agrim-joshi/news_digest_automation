import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey={API_KEY}"

# Make request
r = requests.get(url)

# Get a dictionary with data
content = r.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    print()