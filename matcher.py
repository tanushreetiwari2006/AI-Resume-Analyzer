import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9+#.\s-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def has_skill(skill, text):
    pattern = r"(?<![a-z0-9])" + re.escape(skill.lower()) + r"(?![a-z0-9])"
    return re.search(pattern, text) is not None


def skills_match(resume, jd):
    with open("skills.json") as f:
        skills = json.load(f)
    r = clean(resume)
    j = clean(jd)
    in_jd = [s for s in skills if has_skill(s, j)]
    matched = [s for s in in_jd if has_skill(s, r)]
    missing = [s for s in in_jd if not has_skill(s, r)]
    return matched, missing


def similarity_score(resume, jd):
    vec = TfidfVectorizer(stop_words="english")
    matrix = vec.fit_transform([clean(resume), clean(jd)])
    score = cosine_similarity(matrix[0], matrix[1])[0][0]
    return round(score * 100, 1)