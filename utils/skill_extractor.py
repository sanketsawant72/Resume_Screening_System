def extract_skills(resume_text):
    # Predefined skill set (you can expand this later)
    skills_db = [
        "python", "java", "c", "c++",
        "html", "css", "javascript",
        "sql", "mysql", "mongodb",
        "flask", "django",
        "spring", "spring boot",
        "data structures", "algorithms",
        "machine learning", "deep learning",
        "nlp", "git", "github"
    ]

    found_skills = []

    for skill in skills_db:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills
