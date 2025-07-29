
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd

app = FastAPI()

CSV_PATH = "event_data.csv"

@app.get("/", response_class=HTMLResponse)
async def read_dashboard():
    try:
        df = pd.read_csv(CSV_PATH)
        rows = "".join([f"<tr><td>{r['Názov']}</td><td>{r['Dátum']}</td><td>{r['Cena (€)']}</td><td>{r['Zisk (€)']}</td><td>{r['AttractiScore']}</td><td>{r['Odporúčanie']}</td></tr>" for i, r in df.iterrows()])
    except Exception:
        rows = "<tr><td colspan='6'>Žiadne podujatia</td></tr>"
    with open("style.css") as f:
        style = f.read()
    with open("dashboard.html") as f:
        html = f.read()
    return HTMLResponse(content=html.replace("<!--STYLE-->", f"<style>{style}</style>").replace("<!--DATA-->", rows))
