import streamlit as st
from style import page_head, flow, chips, footer

page_head("How it works", "Four small steps happen behind the Analyze button.")

flow([
    ("Read the PDF", "The pypdf library opens your resume and pulls out the text, page by page."),
    ("Find the skills", "The app looks for skills in the job description (Python, SQL, Docker...) "
                        "and checks which of them appear in your resume. This gives the Skill coverage score."),
    ("Compare the words (TF-IDF)", "Every word gets a weight: common words count less, special words count more. "
                                   "Cosine similarity then tells how close the two texts are. This is the Keyword overlap score."),
    ("Ask the AI", "The resume and job description go to a Gemini model that acts like a recruiter. "
                   "It returns an AI score, strengths, improvements and rewritten bullets. "
                   "If one model is busy, the app tries the next one."),
])

st.markdown('<div class="card"><h4>Built with</h4>'
            + chips(["Python", "Streamlit", "pypdf", "scikit-learn", "TF-IDF", "Gemini API", "Git and GitHub"], "tech")
            + '</div>', unsafe_allow_html=True)

st.markdown('<div class="card"><h4>Why three scores?</h4>'
            '<p style="margin:0;color:#5b6082;line-height:1.5">No single number tells the whole story. '
            'Skill coverage is easy to understand, Keyword overlap is a classic machine learning measure, '
            'and the AI score understands meaning. Together they give a more trustworthy picture.</p></div>',
            unsafe_allow_html=True)
footer()