from parser import extract_text
from ai_feedback import get_feedback

resume = extract_text("resume.pdf")
jd = """We are hiring a Data Analyst. The candidate should know Python,
SQL and pandas, and be able to build dashboards in Power BI or Tableau.
Experience with data analysis, Excel and good communication is required.
Knowledge of Docker is a plus."""

result = get_feedback(resume, jd)
print(result)