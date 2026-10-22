import re

STOPWORDS = {"and", "with", "the", "for", "looking", "experience", "skilled", "developer", "in", "a", "of"}

JOB_DESCRIPTION = "Looking for a Python developer with experience in machine learning, data analysis, SQL and Git."

RESUMES = {
    "Candidate A": "Python developer skilled in machine learning, pandas, data analysis, SQL and Git.",
    "Candidate B": "Java developer with experience in Spring Boot, Android apps and Git.",
    "Candidate C": "Data analyst skilled in Python, SQL, Excel and data analysis.",
}


def tokenize(text):
    words = re.findall(r"[a-z+#]+", text.lower())
    return {w for w in words if len(w) > 2 and w not in STOPWORDS}


def score(resume, job):
    job_words = tokenize(job)
    matched = job_words & tokenize(resume)
    return round(100 * len(matched) / len(job_words), 1), sorted(matched)


if __name__ == "__main__":
    results = []
    for name, text in RESUMES.items():
        s, matched = score(text, JOB_DESCRIPTION)
        results.append((name, s, matched))
    results.sort(key=lambda r: r[1], reverse=True)
    print("Resume Screening Results")
    for rank, (name, s, matched) in enumerate(results, 1):
        print(f"{rank}. {name} - {s}% match - skills: {', '.join(matched)}")
