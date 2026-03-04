def calculate_score(matched_skills, total_job_skills):
    if total_job_skills == 0:
        return 0

    score = (len(matched_skills) / total_job_skills) * 100
    return round(score, 2)


def get_strength_level(score):
    if score >= 75:
        return "Strong"
    elif score >= 40:
        return "Average"
    else:
        return "Weak"
