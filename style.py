import html
import streamlit as st

CSS = """<style>
.hero{background:linear-gradient(135deg,#4f46e5 0%,#7c3aed 55%,#db2777 100%);border-radius:22px;padding:34px 30px;color:#fff;margin-bottom:18px;box-shadow:0 12px 30px rgba(79,70,229,.25)}
.hero h1{margin:8px 0 6px;font-size:2.5rem;line-height:1.1;color:#fff;padding:0}
.hero p{margin:0;font-size:1.05rem;opacity:.93;color:#fff;max-width:560px}
.badge{display:inline-block;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.35);padding:3px 12px;border-radius:999px;font-size:.78rem;letter-spacing:.04em;color:#fff}
.pagehead{margin:4px 0 14px}
.pagehead h2{margin:0;padding:0;font-size:1.8rem;background:linear-gradient(135deg,#4f46e5,#db2777);-webkit-background-clip:text;background-clip:text;color:transparent;display:inline-block}
.pagehead p{margin:4px 0 0;color:#8a8fad}
.steps{display:flex;gap:10px;flex-wrap:wrap;margin:0 0 18px}
.step{flex:1;min-width:150px;background:#fff;color:#1f2340;border:1px solid #e5e7f3;border-radius:14px;padding:10px 14px;font-size:.92rem;box-shadow:0 2px 8px rgba(31,35,64,.05)}
.step b,.num{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:50%;background:#4f46e5;color:#fff;margin-right:8px;font-size:.8rem;font-weight:700}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin:0 0 18px}
.feat{background:#fff;color:#1f2340;border:1px solid #e5e7f3;border-radius:18px;padding:18px;box-shadow:0 6px 22px rgba(31,35,64,.07)}
.feat .ic{font-size:1.7rem;margin-bottom:6px}
.feat h4{margin:0 0 4px;padding:0;font-size:1.02rem;color:#1f2340}
.feat p{margin:0;font-size:.92rem;color:#5b6082;line-height:1.45}
.card{background:#fff;color:#1f2340;border:1px solid #e5e7f3;border-radius:18px;padding:22px;margin:14px 0;box-shadow:0 6px 22px rgba(31,35,64,.07)}
.card h4{margin:0 0 12px;color:#1f2340;font-size:1.05rem;padding:0}
.flow{display:flex;gap:14px;padding:14px 0;border-bottom:1px solid #eef0f8;color:#1f2340}
.flow:last-child{border-bottom:none}
.flow .num{flex:none;width:30px;height:30px;font-size:.95rem;margin:2px 0 0}
.flow h4{margin:0 0 3px;padding:0;font-size:1.02rem;color:#1f2340}
.flow p{margin:0;color:#5b6082;font-size:.93rem;line-height:1.5}
.ringrow{display:flex;justify-content:space-around;flex-wrap:wrap;gap:16px}
.ringbox{text-align:center}
.ring{width:124px;height:124px;border-radius:50%;background:conic-gradient(var(--c) calc(var(--p)*1%),#e8eaf4 0);display:grid;place-items:center;margin:0 auto}
.ring-in{width:94px;height:94px;border-radius:50%;background:#fff;display:grid;place-items:center;font-size:1.5rem;font-weight:700;color:#1f2340}
.ringlabel{margin-top:8px;font-size:.88rem;color:#5b6082}
.verdict{text-align:center;font-weight:700;font-size:1.1rem;margin-top:16px}
.chip{display:inline-block;padding:5px 12px;margin:3px 4px 3px 0;border-radius:999px;font-size:.88rem;font-weight:600}
.chip.ok{background:#dcfce7;color:#166534;border:1px solid #bbf7d0}
.chip.miss{background:#ffe4e6;color:#9f1239;border:1px solid #fecdd3}
.chip.tech{background:#eef2ff;color:#3730a3;border:1px solid #c7d2fe}
.sub{font-size:.8rem;color:#5b6082;margin:12px 0 6px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.item{display:flex;gap:10px;padding:9px 0;border-bottom:1px solid #eef0f8;color:#1f2340;line-height:1.45}
.item:last-child{border-bottom:none}
.dot{flex:none;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;font-size:.75rem;background:#eef2ff;color:#4f46e5;font-weight:700}
.muted{color:#8a8fad}
.footer{text-align:center;color:#8a8fad;font-size:.82rem;margin:26px 0 6px}
.stButton>button{width:100%;border:none;border-radius:14px;padding:.7rem 1rem;background:linear-gradient(135deg,#4f46e5,#db2777)}
.stButton>button p{color:#fff;font-weight:700;font-size:1.02rem}
.stButton>button:hover{filter:brightness(1.08)}
</style>"""


def apply_style():
    st.markdown(CSS, unsafe_allow_html=True)


def to_int(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return None


def color_for(pct):
    if pct >= 70:
        return "#16a34a"
    if pct >= 40:
        return "#f59e0b"
    return "#e11d48"


def ring(pct, label, color):
    pct = max(0, min(100, int(pct)))
    return ('<div class="ringbox"><div class="ring" style="--p:' + str(pct) + ';--c:' + color + '">'
            '<div class="ring-in">' + str(pct) + '%</div></div>'
            '<div class="ringlabel">' + html.escape(label) + '</div></div>')


def chips(items, kind):
    if not items:
        return '<span class="muted">None</span>'
    return "".join('<span class="chip ' + kind + '">' + html.escape(i) + '</span>' for i in items)


def rows(items, icon):
    if not items:
        return '<span class="muted">Nothing to show</span>'
    return "".join('<div class="item"><span class="dot">' + icon + '</span><span>'
                   + html.escape(str(i)) + '</span></div>' for i in items)


def verdict(score):
    if score >= 80:
        return "Excellent match", "#16a34a"
    if score >= 60:
        return "Good match, a few gaps to close", "#d97706"
    return "Needs work for this role", "#e11d48"


def hero(badge, title, text):
    st.markdown('<div class="hero"><span class="badge">' + badge + '</span><h1>'
                + title + '</h1><p>' + text + '</p></div>', unsafe_allow_html=True)


def page_head(title, text):
    st.markdown('<div class="pagehead"><h2>' + title + '</h2><p>' + text + '</p></div>',
                unsafe_allow_html=True)


def feature_grid(items):
    out = '<div class="grid">'
    for icon, title, text in items:
        out += ('<div class="feat"><div class="ic">' + icon + '</div><h4>' + title
                + '</h4><p>' + text + '</p></div>')
    st.markdown(out + '</div>', unsafe_allow_html=True)


def flow(items):
    out = '<div class="card">'
    for i, (title, text) in enumerate(items, start=1):
        out += ('<div class="flow"><span class="num">' + str(i) + '</span><div><h4>' + title
                + '</h4><p>' + text + '</p></div></div>')
    st.markdown(out + '</div>', unsafe_allow_html=True)


def footer():
    st.markdown('<div class="footer">Built with Python, scikit-learn and Gemini. '
                'This app does not save your resume; its text is sent to an AI model to write the feedback.</div>',
                unsafe_allow_html=True)