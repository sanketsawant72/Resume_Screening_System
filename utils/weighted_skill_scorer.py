def calculate_weighted_score(resume_skills, job_skills_with_weight):
    total_weight = 0
    matched_weight = 0
    matched_skills = []
    missing_skills = []

    for skill, weight in job_skills_with_weight.items():
        total_weight += weight

        if skill in resume_skills:
            matched_weight += weight
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if total_weight == 0:
        score = 0
    else:
        score = (matched_weight / total_weight) * 100

    return round(score, 2), matched_skills, missing_skills
