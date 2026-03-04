def analyze_resume_structure(resume_text):
    feedback = []

    text = resume_text.lower()

    # ---- Project Detection ----
    if "project" not in text and "projects" not in text:
        feedback.append(
            "No projects found. Add at least 1–2 academic or personal projects."
        )

    # ---- Internship / Experience Detection ----
    if (
        "internship" not in text
        and "experience" not in text
        and "worked at" not in text
    ):
        feedback.append(
            "No internship or work experience mentioned. Consider adding internships or training experience."
        )

    # ---- Education Detection ----
    education_keywords = ["btech", "b.e", "bachelor", "mca", "degree", "university"]
    if not any(word in text for word in education_keywords):
        feedback.append(
            "Education details are unclear. Mention your degree, college, and graduation year."
        )

    # ---- Resume Length Check ----
    word_count = len(text.split())
    if word_count < 200:
        feedback.append(
            "Resume content is very short. Add more details about skills, projects, and achievements."
        )

    if not feedback:
        feedback.append(
            "Resume structure looks good. Focus on improving skill depth and project quality."
        )

    return feedback
