def generate_feedback(score, missing_skills):
    if score < 40:
        level = "Your resume needs significant improvement."
    elif score < 75:
        level = "Your resume is average and can be improved."
    else:
        level = "Your resume is strong and well-aligned."

    suggestions = []

    if missing_skills:
        suggestions.append("Focus on learning the missing core technical skills.")

    suggestions.append("Add 2–3 relevant projects to your resume.")
    suggestions.append("Optimize resume keywords for ATS systems.")
    suggestions.append("Include measurable achievements instead of descriptions.")

    return level, suggestions
