
import pandas as pd
from datetime import datetime

def fetch_events():
    # Simulácia skutočných dát, neskôr sa nahradí reálnym scrapingom
    events = [
        {"Názov": "The Weeknd - Bratislava", "Dátum": "2025-08-10", "Cena (€)": 89, "Zisk (€)": 42, "AttractiScore": 80, "Odporúčanie": "KÚPIŤ"},
        {"Názov": "Coldplay - Vienna", "Dátum": "2025-08-22", "Cena (€)": 120, "Zisk (€)": 25, "AttractiScore": 74, "Odporúčanie": "NEKÚPIŤ"},
        {"Názov": "Imagine Dragons - Prague", "Dátum": "2025-09-05", "Cena (€)": 99, "Zisk (€)": 51, "AttractiScore": 90, "Odporúčanie": "KÚPIŤ"},
    ]
    df = pd.DataFrame(events)
    df.to_csv("event_data.csv", index=False)

if __name__ == "__main__":
    fetch_events()
