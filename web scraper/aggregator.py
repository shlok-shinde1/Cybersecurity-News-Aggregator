from scrapers.threatpost_scraper import scrape_threatpost
from scrapers.bleeping_scraper import scrape_bleeping_computer

if __name__ == "__main__":
    print("=== Today's Threat Intelligence ===\n")

    print("[ThreatPost]")
    for article in scrape_threatpost():
        print(f"[{article['published']}] {article['title']} - {article['link']}")
    
    print("\n[BleepingComputer]")
    for article in scrape_bleeping_computer():
        print(f"{article['title']} - {article['link']}")