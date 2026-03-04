# from utils.resume_parser import parse_resume
# from utils.skill_extractor import extract_skills
# from utils.skill_gap_analyzer import analyze_skill_gap
# from utils.skill_scorer import calculate_score, get_strength_level
# from utils.resource_recommender import recommend_resources
# from data.job_roles import JOB_ROLES

# resume_path = "data/Sample_resume.pdf"

# # Step 1: Parse resume
# resume_text = parse_resume(resume_path)

# # Step 2: Extract skills
# resume_skills = extract_skills(resume_text)

# # Step 3: Select job role
# job_role = "software_engineer"
# job_skills = JOB_ROLES[job_role]

# # Step 4: Skill gap analysis
# matched, missing = analyze_skill_gap(resume_skills, job_skills)

# # Step 5: Score
# score = calculate_score(matched, len(job_skills))
# strength = get_strength_level(score)

# # Step 6: Resource recommendation
# resources = recommend_resources(missing)

# # Output
# print("\n===== RESUME ANALYSIS REPORT =====")
# print("Target Job Role:", job_role)
# print("Resume Skills:", resume_skills)
# print("Matched Skills:", matched)
# print("Missing Skills:", missing)
# print("Resume Match Percentage:", score, "%")
# print("Resume Strength:", strength)

# print("\n===== RECOMMENDED LEARNING RESOURCES =====")
# for skill, link in resources.items():
#     print(f"{skill} → {link}")

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request
# import os

# from utils.resume_parser import parse_resume
# from utils.skill_extractor import extract_skills
# from utils.skill_gap_analyzer import analyze_skill_gap
# from utils.skill_scorer import calculate_score, get_strength_level
# from utils.resource_recommender import recommend_resources
# from data.job_roles import JOB_ROLES

# app = Flask(__name__)

# UPLOAD_FOLDER = "data"
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         resume_file = request.files.get("resume")
#         job_role = request.form.get("job_role")

#         if resume_file and job_role:
#             # 1. Save resume
#             file_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_file.filename)
#             resume_file.save(file_path)

#             # 2. Run AI pipeline
#             resume_text = parse_resume(file_path)
#             resume_skills = extract_skills(resume_text)

#             job_skills = JOB_ROLES[job_role]
#             matched_skills, missing_skills = analyze_skill_gap(resume_skills, job_skills)

#             score = calculate_score(matched_skills, len(job_skills))
#             strength = get_strength_level(score)

#             resources = recommend_resources(missing_skills)

#             # 3. Send results to UI
#             return render_template(
#                 "result.html",
#                 job_role=job_role,
#                 score=score,
#                 strength=strength,
#                 matched_skills=matched_skills,
#                 missing_skills=missing_skills,
#                 resources=resources
#             )

#     return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, flash
import os

# ----------------- IMPORT CORE LOGIC -----------------
from utils.resume_parser import parse_resume
from utils.skill_extractor import extract_skills
from utils.weighted_skill_scorer import calculate_weighted_score
from utils.skill_scorer import get_strength_level
from utils.resource_recommender import recommend_resources
from utils.feedback_generator import generate_feedback
from utils.resume_structure_analyzer import analyze_resume_structure
from data.job_roles import JOB_ROLES

# ----------------- FLASK APP SETUP -----------------
app = Flask(__name__)
app.secret_key = "resume_analyzer_secret_key"

UPLOAD_FOLDER = "data"
ALLOWED_EXTENSIONS = {"pdf"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ----------------- FILE VALIDATION -----------------
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ----------------- MAIN ROUTE -----------------
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        resume_file = request.files.get("resume")
        job_role = request.form.get("job_role")

        # ---------- VALIDATION ----------
        if not resume_file or resume_file.filename == "":
            flash("Please upload a resume file.", "danger")
            return render_template("index.html")

        if not allowed_file(resume_file.filename):
            flash("Only PDF files are allowed.", "danger")
            return render_template("index.html")

        if not job_role:
            flash("Please select a job role.", "warning")
            return render_template("index.html")

        # ---------- SAVE FILE ----------
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_file.filename)
        resume_file.save(file_path)

        # ---------- AI PIPELINE ----------
        resume_text = parse_resume(file_path)
        resume_skills = extract_skills(resume_text)

        job_skills_with_weight = JOB_ROLES[job_role]

        score, matched_skills, missing_skills = calculate_weighted_score(
            resume_skills,
            job_skills_with_weight
        )

        strength = get_strength_level(score)

        resources = recommend_resources(missing_skills)

        feedback, suggestions = generate_feedback(score, missing_skills)

        structure_feedback = analyze_resume_structure(resume_text)

        # ---------- FINAL RENDER ----------
        return render_template(
            "result.html",
            job_role=job_role,
            score=score,
            strength=strength,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            resources=resources,
            feedback=feedback,
            suggestions=suggestions,
            structure_feedback=structure_feedback
        )

    return render_template("index.html")


# ----------------- RUN SERVER -----------------
if __name__ == "__main__":
    app.run(debug=True)
