from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from zodiac import get_zodiac_sign
from numerology import get_life_path
from chinese_zodiac import get_chinese_zodiac
from astrology import get_astrology_info

app = FastAPI(title="Cosmic Insights API", version="1.0.0")

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BirthData(BaseModel):
    date_of_birth: str       # e.g. "2000-06-15"
    time_of_birth: str = None
    place_of_birth: str = None

@app.get("/")
def root():
    return {
        "message": "Cosmic Insights API is running", 
        "version": "1.0.0",
        "endpoints": {
            "GET /": "API information",
            "POST /analyze": "Get complete astrological analysis",
            "POST /analyze/indian": "Get detailed Indian astrology analysis"
        }
    }

@app.post("/analyze")
def analyze(data: BirthData):
    # Convert date_of_birth string to datetime object
    try:
        dob = datetime.strptime(data.date_of_birth, "%Y-%m-%d").date()
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD."}

    # Basic life stats
    zodiac_sign = get_zodiac_sign(dob)
    life_path_number = get_life_path(dob)
    chinese_zodiac = get_chinese_zodiac(dob.year)
    day_of_week = dob.strftime("%A")

    # Get enhanced astrology info
    astrology_info = get_astrology_info(dob, data.time_of_birth, data.place_of_birth)

    # Determine analysis type
    analysis_type = "Indian Analysis" if data.place_of_birth and any(
        city in data.place_of_birth.lower() for city in ["india", "delhi", "mumbai", "chennai", "kolkata"]
    ) else "Western Analysis"

    return {
        "analysis_type": analysis_type,
        "zodiac_sign": zodiac_sign,
        "life_path_number": life_path_number,
        "chinese_zodiac": chinese_zodiac,
        "day_of_week": day_of_week,
        "astrology_info": astrology_info,
        "birth_details": {
            "date": data.date_of_birth,
            "time": data.time_of_birth,
            "place": data.place_of_birth
        }
    }

@app.post("/analyze/indian")
def analyze_indian(data: BirthData):
    """
    Special endpoint for detailed Indian astrology analysis
    """
    try:
        dob = datetime.strptime(data.date_of_birth, "%Y-%m-%d").date()
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD."}

    # Get Indian astrology info
    from astrology import get_simplified_indian_astrology
    astrology_info = get_simplified_indian_astrology(dob, data.time_of_birth, data.place_of_birth)

    return {
        "analysis_type": "Detailed Indian Astrology",
        "birth_details": {
            "date": data.date_of_birth,
            "time": data.time_of_birth or "Not specified",
            "place": data.place_of_birth or "Not specified"
        },
        "astrology_info": astrology_info
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use Render's port, fallback to 8000 locally
    uvicorn.run(app, host="0.0.0.0", port=port, reload=True)
