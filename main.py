import os
import requests
from dotenv import load_dotenv
from news_utils import send_email

load_dotenv()

TOPIC = os.getenv("NEWS_TOPIC", "tesla")
API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    raise ValueError("NEWS_API_KEY is missing")

news_url = (
    f"https://newsapi.org/v2/everything?"
    f"q={TOPIC}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
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


send_email(
    subject="Today's News",
    body=body,
    recipient=os.getenv("EMAIL_ADDRESS")
)

print("Email sent successfully!")