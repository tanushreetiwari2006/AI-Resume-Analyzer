from parser import extract_text
from matcher import skills_match

resume = extract_text("resume.pdf")
jd = """We need a Data Analyst with Python, SQL, pandas, Tableau,
Power BI and Docker. Good communication is a must."""

matched, missing = skills_match(resume, jd)
print("Matching skills:", matched)
print("Missing skills:", missing)