import os
import pandas as pd
import zipfile

# Debug
print("Current working directory:", os.getcwd())
print("Files in SAMPLE_DATA:", os.listdir("SAMPLE_DATA"))

# Load applicants.csv once
df = pd.read_csv("SAMPLE_DATA/applicants.csv", encoding="utf-8")
print("Applicants data loaded")
print("CSV Columns:", df.columns.tolist())
print(df.head())

# Extract resumes.zip
zip_path = "SAMPLE_DATA/resumes.zip"
extract_path = "SAMPLE_DATA/resumes"

if not os.path.exists(extract_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"Resumes extracted to {extract_path}")
else:
    print("Resumes already extracted.")

# Link resumes (update 'full_name' or 'applicant_id' based on your CSV)
def find_resume(applicant_name):
    for file in os.listdir(extract_path):
        if applicant_name.lower().replace(" ", "_") in file.lower():
            return os.path.join(extract_path, file)
    return None

df["resume_path"] = df["full_name"].apply(find_resume)  # <-- adjust column name here

print("\nApplicants with resume paths:")
print(df[["full_name", "resume_path"]].head())
