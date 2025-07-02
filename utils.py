def matches_keywords(text, keywords):
    text = text.lower()
    return any(k.lower() in text for k in keywords)
