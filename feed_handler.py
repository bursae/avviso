import feedparser
from utils import matches_keywords

def fetch_feed(name, url, keywords, max_articles=5):
    feed = feedparser.parse(url)
    print(f"\n=== {name} ===")
    count = 0

    for entry in feed.entries:
        title = entry.get("title", "")
        summary = entry.get("summary", "")
        content = f"{title} {summary}"

        if matches_keywords(content, keywords):
            print(f"\n• {title}")
            print(f"  Date: {entry.get('published', 'No Date')}")
            print(f"  {summary.strip()[:200]}...")
            print(f"  Link: {entry.link}")
            count += 1

        if count >= max_articles:
            break
