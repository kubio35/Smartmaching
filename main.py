from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    # Uložení obrázku
    with open(f"temp.jpg", "wb") as f:
        shutil.copyfileobj(image.file, f)

    # --- ZDE BUDE JEDNODUCHÁ ANALÝZA --- (zatím jen ukázka)
    result = {
        "partType": "Soustružená osa",
        "material": "Ocel 11 523",
        "totalTime": 42,
        "operations": [
            {"name": "Soustružení", "time": 20, "machine": "Soustruh", "tools": ["nůž ISO", "vrták"]},
            {"name": "Vrtání", "time": 10, "machine": "Vrtačka", "tools": ["vrták Ø12"]},
            {"name": "Broušení", "time": 12, "machine": "Bruska na kulato", "tools": ["kotouč"]},
        ]
    }

    return result