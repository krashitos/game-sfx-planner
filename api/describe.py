"""
Game Sound Effect Planner — Vercel Serverless Function
Powered by Pollinations AI (free, no API keys required)
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

POLLINATIONS_URL = "https://text.pollinations.ai/"


class SFXRequest(BaseModel):
    action: str
    genre: str = "General"


@app.get("/")
async def health():
    return {"status": "Game SFX Planner API is running"}


@app.post("/")
async def describe_sound(request: SFXRequest):
    if not request.action or not request.action.strip():
        raise HTTPException(status_code=400, detail="Action description is required.")

    if len(request.action) > 500:
        raise HTTPException(status_code=400, detail="Action description too long (max 500 chars).")

    prompt = (
        f"You are an expert game sound designer with 20 years of experience crafting audio for AAA titles. "
        f"The game genre is: {request.genre}.\n\n"
        f"A developer asks you to describe the ideal sound effect for this game action:\n"
        f"\"{request.action}\"\n\n"
        f"Provide a DETAILED sound design brief using this EXACT structure (use markdown formatting):\n\n"
        f"## 🎧 Emotional Feel\n"
        f"Describe the emotional impact and mood this sound should evoke in the player. "
        f"How should it make them feel? What psychological response should it trigger?\n\n"
        f"## 🔊 Sound Texture & Character\n"
        f"Describe the raw sonic qualities — is it sharp, smooth, gritty, metallic, organic? "
        f"What real-world sounds does it resemble? Paint the texture with words.\n\n"
        f"## 📊 Frequency Profile\n"
        f"Detail the frequency characteristics:\n"
        f"- **Low end (20-250Hz)**: What role do the bass frequencies play?\n"
        f"- **Mids (250Hz-4kHz)**: What's happening in the body?\n"
        f"- **Highs (4kHz-20kHz)**: What details sit in the upper range?\n\n"
        f"## 🎚️ Layer Breakdown\n"
        f"Break the sound into its component layers:\n"
        f"- **Attack**: The initial transient (first 0-50ms)\n"
        f"- **Body**: The sustained core of the sound\n"
        f"- **Tail/Decay**: How the sound fades and resolves\n"
        f"- **Sweetener**: Any subtle extra layer that adds polish\n\n"
        f"## 🛠️ Production Notes\n"
        f"Recommend specific approaches:\n"
        f"- Synthesis vs. Foley vs. Hybrid?\n"
        f"- Suggested tools or techniques\n"
        f"- Processing chain (reverb, distortion, pitch shift, etc.)\n"
        f"- Duration suggestion\n\n"
        f"## 💡 Pro Tips\n"
        f"2-3 insider tips that would elevate this sound from good to exceptional.\n\n"
        f"Be vivid, specific, and creative. Use sensory language. This brief should be so detailed that "
        f"any sound designer could recreate the exact sound from your description alone."
    )

    try:
        payload = {
            "messages": [{"role": "user", "content": prompt}],
            "model": "openai",
            "jsonMode": False,
        }

        response = requests.post(POLLINATIONS_URL, json=payload, timeout=120)

        if response.status_code == 200:
            # Pollinations may return JSON {"role":"assistant","content":"..."} or plain text
            text = response.text
            try:
                data = json.loads(text)
                if isinstance(data, dict) and "content" in data:
                    text = data["content"]
            except (json.JSONDecodeError, TypeError):
                pass  # Already plain text
            return {"description": text}
        else:
            logger.error(f"Pollinations API error: {response.status_code}")
            raise HTTPException(status_code=500, detail="AI service temporarily unavailable.")

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="AI request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=503, detail="Cannot reach AI service. Check your internet connection.")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
