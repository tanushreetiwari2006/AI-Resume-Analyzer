# ResumeLens: AI Resume Analyzer

Upload a resume, paste a job description, and get a match score, skill gaps and sharper resume bullet points in seconds.

**Live demo:** [add your Streamlit link here after deploying]

## Features

- Reads text from PDF resumes
- **Skill coverage:** which skills in the job description are present or missing in the resume
- **Keyword overlap:** a TF-IDF and cosine similarity score between resume and job description
- **AI feedback:** an AI score, strengths, improvements and rewritten resume bullets using the Gemini API
- Automatic fallback: if one AI model is busy, the app tries the next one
- 4-page web app: Home, Analyzer, How it works, Tips (with a resume checklist)

## Tech stack

Python, Streamlit, pypdf, scikit-learn (TF-IDF), Gemini API, Git and GitHub

## How it works

1. `parser.py` extracts text from the PDF with pypdf
2. `matcher.py` finds skills (from `skills.json`) and calculates the TF-IDF similarity
3. `ai_feedback.py` sends the resume and job description to a Gemini model and reads the JSON reply
4. `app.py` and the page files build the Streamlit website

## Run it on your computer

```bash
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Create a `.env` file in the project folder with your own key:

```
GEMINI_API_KEY=your_key_here
```

Get a free key from Google AI Studio. Never share your key or upload `.env` to GitHub.

## What I learned

- Extracting and cleaning text from PDFs
- Classic NLP with TF-IDF and cosine similarity
- Calling an AI API, writing prompts and handling errors, timeouts and busy servers
- Building and deploying a multi-page web app
- Keeping secrets safe (`.env`, `.gitignore`)

## Limitations

- Works only with text-based PDFs (not scanned images)
- The skill list in `skills.json` is limited, so some skills may not be detected
- Free AI tiers can be slow or busy at times

## Author

[Your name] | [LinkedIn link] | [GitHub link]