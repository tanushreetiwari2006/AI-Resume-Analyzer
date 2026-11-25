import json
import os
import urllib.request
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

request = urllib.request.Request(
    "https://generativelanguage.googleapis.com/v1beta/models?pageSize=100",
    headers={"x-goog-api-key": api_key},
)
with urllib.request.urlopen(request, timeout=30) as response:
    data = json.loads(response.read().decode("utf-8"))

for m in data["models"]:
    if "generateContent" in m.get("supportedGenerationMethods", []):
        print(m["name"])