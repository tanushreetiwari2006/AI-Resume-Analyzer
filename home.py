import streamlit as st
from style import hero, feature_grid, footer

hero("AI-powered &middot; Free", "ResumeLens",
     "See your resume the way a recruiter does. Get a match score, skill gaps "
     "and sharper bullet points in seconds.")

feature_grid([
    ("📄", "Smart PDF reading", "Upload your resume and ResumeLens reads the text for you."),
    ("🎯", "Skill gap finder", "See which skills the job asks for and which ones your resume is missing."),
    ("🤖", "AI feedback", "Get strengths, improvements and rewritten bullet points from an AI recruiter."),
])

st.markdown(
    '<div class="steps">'
    '<div class="step"><b>1</b>Upload resume</div>'
    '<div class="step"><b>2</b>Paste job description</div>'
    '<div class="step"><b>3</b>Get insights</div></div>',
    unsafe_allow_html=True,
)

st.page_link("analyzer.py", label="Analyze my resume", icon="🚀")
footer()