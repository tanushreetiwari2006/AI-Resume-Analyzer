import json
import os
import time
import urllib.request
import urllib.error
from dotenv import load_dotenv

load_dotenv()

# Pehle upar wala model try hoga, na chale to agla
MODELS = [
    "gemini-3.5-flash",
    "gemini-3.7-flash",
    "gemini-3.8-flash",
    "gemini-3.5-flash-lite",
    "gemini-flash-latest",
]

PROMPT = """You are an expert recruiter. Compare the resume with the job description.
Return ONLY valid JSON (no extra text, no markdown) with these keys:
- "match_score": a number from 0 to 100
- "strengths": a list of at most 3 short strings
- "improvements": a list of at most 5 specific, actionable strings
- "rewritten_bullets": a list of 3 improved resume bullet points

Resume:
{resume}

Job Description:
{jd}
"""


def ask_model(model, body, api_key):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    request = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": api_key},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data["candidates"][0]["content"]["parts"][0]["text"]


def get_feedback(resume, jd):
    api_key = os.getenv("GEMINI_API_KEY")
    body = {
        "contents": [{"parts": [{"text": PROMPT.format(resume=resume, jd=jd)}]}],
        "generationConfig": {"responseMimeType": "application/json"},
    }

    for model in MODELS:
        for attempt in (1, 2):
            try:
                text = ask_model(model, body, api_key)
                text = text.replace("```json", "").replace("```", "").strip()
                print("Kaam kiya:", model)
                return json.loads(text)
            except urllib.error.HTTPError as e:
                print(model, "-> HTTP error", e.code)
                if e.code in (429, 500, 503) and attempt == 1:
                    time.sleep(8)
                    continue
                break
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                print(model, "-> network ya timeout problem:", type(e).__name__)
                break
            except (KeyError, IndexError, json.JSONDecodeError):
                print(model, "-> jawab samajh nahi aaya")
                break
    return None