import streamlit as st
from parser import extract_text
from matcher import similarity_score, skills_match
from ai_feedback import get_feedback
from style import (page_head, ring, chips, rows, verdict, color_for, to_int, footer)

page_head("Analyzer", "Upload your resume, paste a job description and get your results.")

left, right = st.columns(2)
with left:
    file = st.file_uploader("Your resume (PDF)", type="pdf")
with right:
    jd = st.text_area("Job description", height=170,
                      placeholder="Paste the full job description here...")

go = st.button("Analyze my resume", type="primary")

if go:
    if file is None or not jd.strip():
        st.warning("Pehle resume upload karo aur job description paste karo.")
        st.stop()

    resume = extract_text(file)
    if len(resume) < 100:
        st.error("Is PDF se text nahi nikla. Text-based PDF use karo (scan ki hui nahi).")
        st.stop()

    overlap = similarity_score(resume, jd)
    matched, missing = skills_match(resume, jd)
    total = len(matched) + len(missing)
    coverage = round(len(matched) / total * 100) if total else None

    with st.spinner("AI aapka resume padh raha hai..."):
        result = get_feedback(resume, jd)

    ai_score = to_int(result.get("match_score")) if result else None

    rings = ""
    if coverage is not None:
        rings += ring(coverage, "Skill coverage", color_for(coverage))
    rings += ring(overlap, "Keyword overlap", "#4f46e5")
    if ai_score is not None:
        rings += ring(ai_score, "AI match score", color_for(ai_score))

    main_score = ai_score if ai_score is not None else coverage
    verdict_html = ""
    if main_score is not None:
        text, vcolor = verdict(main_score)
        verdict_html = '<div class="verdict" style="color:' + vcolor + '">' + text + '</div>'

    st.markdown('<div class="card"><h4>Your results</h4><div class="ringrow">'
                + rings + '</div>' + verdict_html + '</div>', unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Skills", "AI feedback", "Better bullets"])

    with tab1:
        if total == 0:
            st.info("Job description me hamari skills list ka koi skill nahi mila. "
                    "Pura job description paste karo, jisme skills likhe hon (jaise Python, SQL).")
        else:
            st.markdown('<div class="card"><div class="sub">You have</div>' + chips(matched, "ok")
                        + '<div class="sub">Missing from your resume</div>' + chips(missing, "miss")
                        + '</div>', unsafe_allow_html=True)

    with tab2:
        if result:
            st.markdown('<div class="card"><div class="sub">Strengths</div>'
                        + rows(result.get("strengths", []), "&#10003;")
                        + '<div class="sub">What to improve</div>'
                        + rows(result.get("improvements", []), "&#8599;")
                        + '</div>', unsafe_allow_html=True)
        else:
            st.warning("AI abhi jawab nahi de paaya (server busy ho sakta hai). Thodi der baad dobara try karo.")

    with tab3:
        if result:
            st.markdown('<div class="card"><div class="sub">Rewrite these on your resume</div>'
                        + rows(result.get("rewritten_bullets", []), "&#9733;")
                        + '</div>', unsafe_allow_html=True)
        else:
            st.warning("AI abhi jawab nahi de paaya. Thodi der baad dobara try karo.")

footer()