# CareerAI – Personalized Career Development Assistant

A full-stack career guidance application that analyzes a student's skills, interests and career goals and generates:

- Personalized professional summary
- Career suitability scores
- Skill-gap analysis
- Personalized learning roadmap
- Interview preparation questions
- Recommended projects
- Progress tracking

## Tech Stack
- Python + Flask backend
- HTML/CSS/JavaScript frontend
- Rule-based career intelligence and skill matching engine
- Local browser storage for progress tracking

## Run the project

### 1. Open the project folder in VS Code

### 2. Create a virtual environment
```powershell
python -m venv venv
```

### 3. Activate it
```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install packages
```powershell
pip install -r requirements.txt
```

### 5. Start the application
```powershell
python app.py
```

Open:

`http://127.0.0.1:5000`

## How the intelligence works

The application first creates a structured **Master Career Profile**. Every generated section uses this same analysis, which keeps the professional summary, skill-gap report, roadmap and interview preparation consistent.

The backend:
1. Normalizes student skills and interests.
2. Compares them with role-specific skill requirements.
3. Calculates weighted career suitability scores.
4. Identifies strengths, partial matches and missing skills.
5. Builds a personalized roadmap based on missing priority skills.
6. Generates role-specific interview preparation.

## Main supported career paths
- Software Developer
- AI/ML Engineer
- Data Analyst
- Frontend Developer
- Backend Developer
- Data Scientist

You can extend `career_engine.py` to add more roles.
