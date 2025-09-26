import streamlit as st
import requests

st.title("Applicant Scoring Demo")

skills = st.slider("Skills alignment", 0.0, 1.0, 0.7)
exp = st.number_input("Years experience", 0, 10, 2)
assess = st.slider("Assessments", 0.0, 1.0, 0.6)
sim = st.slider("Semantic similarity", 0.0, 1.0, 0.5)
edu = st.slider("Education level norm", 0.0, 1.0, 0.4)

if st.button("Score"):
    data = {
        "skills_alignment": skills,
        "years_experience": exp,
        "assessments_norm": assess,
        "semantic_similarity": sim,
        "education_level_norm": edu
    }
    res = requests.post("http://localhost:8000/score", json=data)
    st.json(res.json())