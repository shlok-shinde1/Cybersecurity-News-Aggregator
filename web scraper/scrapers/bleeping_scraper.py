import requests
from bs4 import BeautifulSoup

def scrape_bleeping_computer():
    url = "https://www.bleepingcomputer.com/"

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"
    }

    try:
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching BleepingComputer: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    # Look inside both the "Featured" and "Latest" tabs
    featured = soup.select("#nfeatured li")
    latest = soup.select("#nlatest li")

    # Combine them and get up to 5 articles
    all_articles = (featured + latest)[:5]

    if not all_articles:
        print("No articles found in #nfeatured or #nlatest.")
        return articles

    for item in all_articles:
        a_tag = item.find('a', href=True)
        p_tag = a_tag.find('p') if a_tag else None

        if a_tag and p_tag:
            link = a_tag['href']
            # Ensure link is absolute
            if link.startswith("/"):
                link = url.rstrip('/') + link
            title = p_tag.get_text(strip=True)
            
            articles.append({
                'title': title,
                'link': link
            })

    return articles

