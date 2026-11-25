import streamlit as st
from style import apply_style

st.set_page_config(page_title="ResumeLens", page_icon="🔍")
apply_style()

pages = [
    st.Page("home.py", title="Home", icon="🏠", default=True),
    st.Page("analyzer.py", title="Analyzer", icon="📄"),
    st.Page("how_it_works.py", title="How it works", icon="⚙️"),
    st.Page("tips.py", title="Tips", icon="💡"),
]

try:
    nav = st.navigation(pages, position="top")
except TypeError:
    nav = st.navigation(pages)

nav.run()