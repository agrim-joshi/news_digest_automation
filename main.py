import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    raise ValueError("NEWS_API_KEY is missing")

news_url = (
    f"https://newsapi.org/v2/everything?"
    f"q=tesla&sortBy=publishedAt&apiKey={API_KEY}"
)

response = requests.get(news_url, timeout=10)
response.raise_for_status()

content = response.json()

body = "Subject: Today's News\n\n"

for article in content["articles"][:20]:
    title = article.get("title")
    description = article.get("description")
    article_url = article.get("url")

    if title:
        body += f"{title}\n"
        body += f"{description or 'No description available'}\n"
        body += f"{article_url}\n\n"

body = body.encode("utf-8")

print(body)