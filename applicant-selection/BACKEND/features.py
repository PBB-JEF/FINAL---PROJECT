from typing import Dict

def normalize(v, vmin, vmax):
    if vmax == vmin: return 0.0
    return max(0.0, min(1.0, (v - vmin) / (vmax - vmin)))

def score_candidate(f: Dict, weights: Dict) -> Dict:
    comp = {
        "skills_alignment": f.get("skills_alignment", 0.0),
        "assessments_norm": f.get("assessments_norm", 0.0),
        "exp_years_norm": normalize(f.get("years_experience",0), 0, 5),
        "semantic_similarity": f.get("semantic_similarity", 0.0),
        "education_level_norm": f.get("education_level_norm", 0.0),
    }
    weighted = sum(weights[k] * comp[k] for k in weights)
    overall = round(100 * weighted, 1)
    return {"overall": overall, "breakdown": comp}