
import requests
from bs4 import BeautifulSoup
import csv

def fetch_see_tickets():
    url = "https://www.seetickets.com/tour/the-weeknd"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    events = []
    for event in soup.select(".event-item"):
        try:
            name = event.select_one(".event-name").get_text(strip=True)
            date = event.select_one(".event-date").get_text(strip=True)
            price = event.select_one(".event-price").get_text(strip=True) if event.select_one(".event-price") else "N/A"
            events.append({"name": name, "date": date, "price": price})
        except:
            continue

    return events

def save_to_csv(events, filename="event_data.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "date", "price"])
        writer.writeheader()
        for event in events:
            writer.writerow(event)

if __name__ == "__main__":
    events = fetch_see_tickets()
    save_to_csv(events)
