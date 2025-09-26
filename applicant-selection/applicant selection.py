applicant-selection/
│── backend/               # FastAPI app
│   ├── main.py             # Entry point (API routes)
│   ├── features.py         # Scoring logic (pseudocode from blueprint)
│   ├── models.py           # SQLAlchemy models (tables: applicants, artifacts, scores…)
│   ├── database.py         # DB connection setup
│   ├── schemas.py          # Pydantic schemas for request/response
│   └── requirements.txt    # Python dependencies
│
│── frontend/              # Simple React or Streamlit UI
│   ├── streamlit_app.py    # (if using Streamlit)
│   └── package.json        # (if using React)
│
│── docker-compose.yml      # Runs backend + Postgres + MinIO
│── README.md               # Setup & run instructions
│── sample_data/            # CSVs/resumes to test
│   ├── applicants.csv
│   └── resumes.zip