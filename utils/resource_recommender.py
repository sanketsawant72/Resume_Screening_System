def recommend_resources(missing_skills):
    resources = {
        "c++": "https://www.geeksforgeeks.org/c-plus-plus/",
        "java": "https://www.javatpoint.com/java-tutorial",
        "python": "https://www.learnpython.org/",
        "data structures": "https://www.geeksforgeeks.org/data-structures/",
        "algorithms": "https://www.geeksforgeeks.org/fundamentals-of-algorithms/",
        "sql": "https://www.w3schools.com/sql/",
        "html": "https://www.w3schools.com/html/",
        "css": "https://www.w3schools.com/css/",
        "javascript": "https://www.w3schools.com/js/",
        "git": "https://git-scm.com/doc"
    }

    recommendations = {}

    for skill in missing_skills:
        if skill in resources:
            recommendations[skill] = resources[skill]
        else:
            recommendations[skill] = "Resource not available yet"

    return recommendations
