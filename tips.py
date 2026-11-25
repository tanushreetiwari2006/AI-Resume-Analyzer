import streamlit as st
from style import page_head, feature_grid, footer

page_head("Tips", "Small changes that make a resume work better with recruiters and ATS software.")

feature_grid([
    ("🎯", "Match the job", "Use the same skill words that the job description uses, as long as they are true for you."),
    ("📊", "Show numbers", "Write results, not duties. Example: cut report time by 30%."),
    ("📄", "Keep it simple", "One column, normal fonts and no images. ATS software reads plain layouts best."),
    ("✏️", "Start with action words", "Built, analysed, automated, led. One line per achievement."),
])

st.markdown('<div class="sub">Your resume checklist</div>', unsafe_allow_html=True)

CHECKLIST = [
    "My resume is one page (freshers) and saved as a text-based PDF",
    "My name, email, phone and GitHub or LinkedIn link are at the top",
    "I added a short career objective or summary",
    "My skills match the job description",
    "Every project says what I built, which tools I used and the result",
    "I used numbers wherever possible (accuracy, time saved, users)",
    "There are no spelling mistakes",
    "I checked my resume with the Analyzer page",
]

done = 0
for i, item in enumerate(CHECKLIST):
    if st.checkbox(item, key="check" + str(i)):
        done += 1

st.progress(done / len(CHECKLIST))
st.caption(str(done) + " of " + str(len(CHECKLIST)) + " done")
footer()