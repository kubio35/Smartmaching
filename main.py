import os
import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

app = FastAPI()

# 📌 Povolení CORS, aby frontend mohl komunikovat s backendem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Lepší je zadat přesnou URL frontendu pro vyšší bezpečnost
    allow_methods=["POST"],
    allow_headers=["*"]
)

@app.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    # Uložení obrázku do dočasného souboru
    image_path = "temp.jpg"
    with open(image_path, "wb") as f:
        shutil.copyfileobj(image.file, f)

    # 🛠 Simulovaná analýza součástky
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

# 🚀 Dynamické nastavení portu pro Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render automaticky nastaví správný port
    uvicorn.run(app, host="0.0.0.0", port=port)
