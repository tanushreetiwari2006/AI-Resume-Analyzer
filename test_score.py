from parser import extract_text
from matcher import skills_match, similarity_score

resume = extract_text("resume.pdf")
jd = """We are hiring a Data Analyst. The candidate should know Python,
SQL and pandas, and be able to build dashboards in Power BI or Tableau.
Experience with data analysis, Excel and good communication is required.
Knowledge of Docker is a plus."""

score = similarity_score(resume, jd)
matched, missing = skills_match(resume, jd)

print("Similarity score:", score, "%")
print("Matching skills:", matched)
print("Missing skills:", missing)