from fastapi import FastAPI
from features import score_candidate

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend running"}

@app.post("/score")
def score_applicant(applicant: dict):
    # In reality you'd pull features from DB
    weights = {
        "skills_alignment":0.35,
        "exp_years_norm":0.25,
        "assessments_norm":0.25,
        "semantic_similarity":0.10,
        "education_level_norm":0.05
    }
    return score_candidate(applicant, weights)