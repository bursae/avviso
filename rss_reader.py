from feeds import RSS_FEEDS
from feed_handler import fetch_feed

def load_keywords(filename="keywords.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        # Flatten all keywords from both comma- and line-separated formats
        keywords = []
        for line in lines:
            keywords.extend([k.strip() for k in line.strip().split(",") if k.strip()])
        return keywords
    except FileNotFoundError:
        print(f"⚠️  Keyword file '{filename}' not found.")
        return []

def main():
    print("🔎 NJ & Bergen County News – Keyword Filtered (saved keywords)")

    keywords = load_keywords()

    if not keywords:
        print("No keywords found. Please add them to keywords.txt.")
        return

    print(f"Using keywords: {', '.join(keywords)}")

    for name, url in RSS_FEEDS:
        fetch_feed(name, url, keywords)

if __name__ == "__main__":
    main()
