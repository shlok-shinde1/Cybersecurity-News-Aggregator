import feedparser

def scrape_threatpost():
    # Scrape the latest articles from ThreatPost's RSS Feed.
    url = "https://threatpost.com/feed/"
    feed = feedparser.parse(url)
    articles = []
    
    for entry in feed.entries[:5]: # limit to the latest 5 articles
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published
        })
        
    return articles