import re


# ============================================================
# CAREER DATABASE
# ============================================================

CAREERS = {
    "Software Developer": {
        "skills": [
            "python", "java", "c", "c++",
            "data structures", "algorithms",
            "oop", "git", "github", "sql",
            "debugging"
        ],
        "keywords": [
            "software", "programming", "development",
            "applications", "coding"
        ],
        "projects": [
            "Task Management System",
            "Student Management System",
            "Full-Stack Web Application"
        ]
    },

    "AI/ML Engineer": {
        "skills": [
            "python",
            "data structures",
            "statistics",
            "numpy",
            "pandas",
            "machine learning",
            "scikit-learn",
            "deep learning",
            "tensorflow",
            "pytorch",
            "sql"
        ],
        "keywords": [
            "ai", "artificial intelligence",
            "machine learning", "ml",
            "computer vision", "data"
        ],
        "projects": [
            "AI Career Recommendation System",
            "Student Performance Prediction System",
            "Image Classification Application"
        ]
    },

    "Data Analyst": {
        "skills": [
            "python",
            "sql",
            "excel",
            "pandas",
            "statistics",
            "power bi",
            "tableau",
            "data visualization"
        ],
        "keywords": [
            "data", "analytics", "analysis",
            "business intelligence"
        ],
        "projects": [
            "Sales Analytics Dashboard",
            "Student Performance Dashboard",
            "Customer Data Analysis System"
        ]
    },

    "Frontend Developer": {
        "skills": [
            "html",
            "css",
            "javascript",
            "react",
            "responsive design",
            "git",
            "github",
            "api"
        ],
        "keywords": [
            "frontend", "web", "ui",
            "website", "user interface"
        ],
        "projects": [
            "Personal Portfolio Website",
            "E-commerce Frontend",
            "Interactive Dashboard"
        ]
    },

    "Backend Developer": {
        "skills": [
            "python",
            "java",
            "node.js",
            "express",
            "flask",
            "sql",
            "mongodb",
            "api",
            "authentication",
            "git"
        ],
        "keywords": [
            "backend", "server",
            "api", "database"
        ],
        "projects": [
            "REST API Platform",
            "Authentication System",
            "Backend for a Social Media Application"
        ]
    },

    "Data Scientist": {
        "skills": [
            "python",
            "statistics",
            "machine learning",
            "pandas",
            "numpy",
            "sql",
            "data visualization",
            "scikit-learn"
        ],
        "keywords": [
            "data science",
            "data",
            "machine learning",
            "statistics",
            "analytics"
        ],
        "projects": [
            "Predictive Analytics System",
            "Customer Segmentation System",
            "Recommendation Engine"
        ]
    }
}


# ============================================================
# SKILL ALIASES
# ============================================================

ALIASES = {
    "js": "javascript",
    "react.js": "react",
    "node": "node.js",
    "nodejs": "node.js",

    "ml": "machine learning",
    "ai": "artificial intelligence",

    "dsa": "data structures",
    "leetcode": "data structures",

    "mysql": "sql",
    "postgresql": "sql",
    "postgres": "sql",

    "sklearn": "scikit-learn",

    "object oriented programming": "oop",
    "object-oriented programming": "oop"
}


# ============================================================
# LEARNING CONTENT
# ============================================================

SKILL_LEARNING_PLANS = {

    "python": [
        "Revise Python syntax, variables and data types",
        "Practice conditions, loops and functions",
        "Learn lists, dictionaries, sets and tuples",
        "Practice file handling and exception handling",
        "Revise OOP concepts in Python",
        "Solve Python programming problems",
        "Build a small Python mini-project"
    ],

    "java": [
        "Revise Java syntax and OOP fundamentals",
        "Practice classes, objects and constructors",
        "Learn inheritance and polymorphism",
        "Practice exception handling",
        "Solve Java programming problems"
    ],

    "data structures": [
        "Learn arrays and strings",
        "Practice linked lists",
        "Learn stacks and queues",
        "Practice recursion",
        "Learn trees and binary search trees",
        "Understand graphs",
        "Solve DSA problems"
    ],

    "algorithms": [
        "Learn time and space complexity",
        "Practice searching algorithms",
        "Practice sorting algorithms",
        "Learn recursion and backtracking",
        "Practice dynamic programming fundamentals"
    ],

    "statistics": [
        "Learn mean, median and mode",
        "Study variance and standard deviation",
        "Learn probability fundamentals",
        "Understand probability distributions",
        "Learn correlation and covariance",
        "Study hypothesis testing",
        "Practice statistical analysis"
    ],

    "numpy": [
        "Learn NumPy arrays",
        "Practice array operations",
        "Learn indexing and slicing",
        "Practice mathematical operations using NumPy"
    ],

    "pandas": [
        "Learn Pandas Series and DataFrames",
        "Practice loading CSV datasets",
        "Handle missing values",
        "Perform data filtering and grouping",
        "Practice data analysis using a real dataset"
    ],

    "sql": [
        "Learn SELECT, WHERE and ORDER BY",
        "Practice aggregate functions",
        "Learn GROUP BY and HAVING",
        "Practice JOIN operations",
        "Learn subqueries",
        "Practice database problems"
    ],

    "machine learning": [
        "Understand Machine Learning fundamentals",
        "Learn supervised vs unsupervised learning",
        "Practice train-test split",
        "Learn Linear Regression",
        "Learn Logistic Regression",
        "Learn Decision Trees and Random Forest",
        "Practice model evaluation"
    ],

    "scikit-learn": [
        "Learn the Scikit-learn workflow",
        "Load and preprocess datasets",
        "Train your first ML model",
        "Evaluate model performance",
        "Compare multiple models"
    ],

    "deep learning": [
        "Understand neural network fundamentals",
        "Learn activation functions",
        "Study forward and backpropagation",
        "Build a basic neural network",
        "Learn deep learning model evaluation"
    ],

    "tensorflow": [
        "Understand TensorFlow basics",
        "Build a simple neural network",
        "Train and evaluate a TensorFlow model",
        "Build a small deep learning project"
    ],

    "pytorch": [
        "Understand PyTorch tensors",
        "Learn neural network modules",
        "Train a PyTorch model",
        "Evaluate model performance"
    ],

    "html": [
        "Learn HTML document structure",
        "Practice semantic HTML",
        "Build page layouts"
    ],

    "css": [
        "Learn CSS selectors and styling",
        "Practice Flexbox",
        "Practice CSS Grid",
        "Build responsive layouts"
    ],

    "javascript": [
        "Revise JavaScript fundamentals",
        "Learn functions and ES6",
        "Practice arrays and objects",
        "Learn asynchronous JavaScript",
        "Work with APIs"
    ],

    "react": [
        "Learn React components",
        "Practice props and state",
        "Learn React hooks",
        "Practice API integration",
        "Build a React project"
    ],

    "node.js": [
        "Learn Node.js fundamentals",
        "Understand npm and modules",
        "Build a simple backend server",
        "Create REST APIs"
    ],

    "express": [
        "Learn Express routing",
        "Build REST APIs",
        "Implement middleware",
        "Add error handling"
    ],

    "flask": [
        "Learn Flask application structure",
        "Create routes and APIs",
        "Handle JSON requests",
        "Connect Flask to a database"
    ],

    "mongodb": [
        "Learn MongoDB fundamentals",
        "Understand collections and documents",
        "Perform CRUD operations",
        "Connect MongoDB to an application"
    ],

    "api": [
        "Understand REST API concepts",
        "Learn HTTP methods",
        "Practice JSON requests and responses",
        "Build and test an API"
    ],

    "authentication": [
        "Understand authentication concepts",
        "Learn password security",
        "Understand JWT",
        "Implement login and protected routes"
    ],

    "git": [
        "Learn Git fundamentals",
        "Practice add, commit and status",
        "Learn branches",
        "Practice push and pull"
    ],

    "github": [
        "Create and organize repositories",
        "Push projects to GitHub",
        "Learn pull requests",
        "Improve project documentation"
    ]
}


# ============================================================
# HELPERS
# ============================================================

def normalize(value):

    value = value.strip().lower()

    return ALIASES.get(value, value)


def split_items(value):

    if isinstance(value, list):
        items = value
    else:
        items = re.split(r"[,;\n]", str(value))

    result = []

    for item in items:

        item = normalize(str(item))

        if item:
            result.append(item)

    return result


# ============================================================
# CAREER MATCH SCORE
# ============================================================

def calculate_role_score(user_skills, interests, role_name, goal):

    role = CAREERS[role_name]

    required_skills = set(role["skills"])

    matched_skills = set(user_skills) & required_skills

    skill_score = (
        len(matched_skills) /
        len(required_skills)
    ) * 70

    text = " ".join(
        interests + [goal]
    ).lower()

    keyword_hits = sum(

        1 for keyword in role["keywords"]

        if keyword in text

    )

    interest_score = min(
        keyword_hits * 8,
        30
    )

    if goal.lower() == role_name.lower():

        interest_score = min(
            interest_score + 10,
            30
        )

    total = min(
        skill_score + interest_score,
        100
    )

    return round(total), list(matched_skills)


# ============================================================
# PROFESSIONAL SUMMARY
# ============================================================

def generate_professional_summary(
    name,
    education,
    target_role,
    strengths,
    gaps,
    interests,
    experience
):

    strength_text = ", ".join(
        skill.title()
        for skill in strengths[:4]
    )

    interest_text = ", ".join(
        interest.title()
        for interest in interests[:3]
    )

    gap_text = ", ".join(
        skill.title()
        for skill in gaps[:4]
    )

    if not strength_text:
        strength_text = "programming and technical learning"

    if not interest_text:
        interest_text = "technology and professional development"

    summary = (
        f"{name} is an aspiring {target_role} "
        f"with a growing foundation in {strength_text}. "
    )

    if education:

        summary += (
            f"Currently pursuing {education}, "
        )

    summary += (
        f"with strong interests in {interest_text}. "
    )

    summary += (
        f"As a {experience.lower()} learner, "
        f"the current profile demonstrates a developing "
        f"technical foundation and a clear direction "
        f"towards a career in {target_role}. "
    )

    if gaps:

        summary += (
            f"The next stage of professional development "
            f"should focus on strengthening {gap_text}. "
        )

    summary += (
        "By following a structured learning plan, "
        "building practical projects, maintaining consistent "
        "problem-solving practice and preparing for technical "
        "interviews, the candidate can progressively develop "
        "the skills required for internships and entry-level "
        "opportunities in the selected career path."
    )

    return summary


# ============================================================
# PERSONALIZED DAY-WISE ROADMAP
# ============================================================

def generate_daywise_roadmap(
    missing_skills,
    existing_skills,
    target_role,
    total_days
):

    roadmap = []

    day = 1

    # --------------------------------------------------------
    # If student has no major missing skills
    # --------------------------------------------------------

    if not missing_skills:

        missing_skills = [
            "advanced projects",
            "interview preparation"
        ]

    # --------------------------------------------------------
    # Calculate learning days
    # --------------------------------------------------------

    if total_days == 30:

        learning_percentage = 0.65
        project_percentage = 0.20

    elif total_days == 60:

        learning_percentage = 0.70
        project_percentage = 0.20

    else:

        learning_percentage = 0.70
        project_percentage = 0.20

    learning_days = int(
        total_days * learning_percentage
    )

    project_days = int(
        total_days * project_percentage
    )

    interview_days = (
        total_days
        - learning_days
        - project_days
    )

    # --------------------------------------------------------
    # Personalized learning phase
    # --------------------------------------------------------

    skills_to_learn = missing_skills[:8]

    days_per_skill = max(
        2,
        learning_days // len(skills_to_learn)
    )

    for skill in skills_to_learn:

        tasks = SKILL_LEARNING_PLANS.get(

            skill,

            [
                f"Understand the fundamentals of {skill.title()}",
                f"Study important concepts in {skill.title()}",
                f"Practice hands-on exercises using {skill.title()}",
                f"Complete a mini practical task using {skill.title()}"
            ]

        )

        skill_start = day

        for i in range(days_per_skill):

            if day > learning_days:
                break

            task = tasks[
                i % len(tasks)
            ]

            roadmap.append({

                "day": day,

                "phase": "Skill Development",

                "skill": skill.title(),

                "task": task

            })

            day += 1

        # Add revision day periodically

        if (
            day % 7 == 0
            and day <= learning_days
        ):

            roadmap.append({

                "day": day,

                "phase": "Revision",

                "skill": "Weekly Revision",

                "task":
                    f"Revise the concepts learned during the previous days and solve practice problems related to {skill.title()}."

            })

            day += 1

    # --------------------------------------------------------
    # Fill remaining learning days
    # --------------------------------------------------------

    while day <= learning_days:

        roadmap.append({

            "day": day,

            "phase": "Practice",

            "skill": "Practical Practice",

            "task":
                "Practice previously learned concepts, solve problems and improve weak areas."

        })

        day += 1

    # --------------------------------------------------------
    # PROJECT PHASE
    # --------------------------------------------------------

    project_tasks = [

        "Choose a project idea related to your target career and define the problem statement.",

        "Research similar solutions and plan the features of your project.",

        "Set up the development environment and create the project structure.",

        "Implement the core functionality of the project.",

        "Continue development and add important features.",

        "Test the project using different inputs and fix errors.",

        "Improve the user experience and optimize the implementation.",

        "Create proper documentation and prepare a GitHub repository.",

        "Review the completed project and prepare to explain it in an interview."

    ]

    project_end = (
        learning_days + project_days
    )

    project_index = 0

    while day <= project_end:

        roadmap.append({

            "day": day,

            "phase": "Project Development",

            "skill": f"{target_role} Project",

            "task":
                project_tasks[
                    project_index
                    % len(project_tasks)
                ]

        })

        project_index += 1

        day += 1

    # --------------------------------------------------------
    # INTERVIEW PHASE
    # --------------------------------------------------------

    interview_tasks = [

        "Revise your professional summary and practice introducing yourself.",

        "Review important technical concepts required for your target role.",

        "Solve technical and problem-solving questions.",

        "Practice explaining your projects clearly.",

        "Prepare answers for common HR interview questions.",

        "Practice role-specific technical interview questions.",

        "Conduct a mock interview and identify weak areas.",

        "Revise weak areas and improve your answers.",

        "Review your resume, GitHub projects and career portfolio."

    ]

    interview_index = 0

    while day <= total_days:

        roadmap.append({

            "day": day,

            "phase": "Interview Preparation",

            "skill": "Career Preparation",

            "task":
                interview_tasks[
                    interview_index
                    % len(interview_tasks)
                ]

        })

        interview_index += 1

        day += 1

    return roadmap


# ============================================================
# INTERVIEW QUESTIONS
# ============================================================

def generate_interview_questions(
    role,
    strengths,
    gaps,
    projects
):

    common_questions = [

        "Tell me about yourself and explain how your background relates to your target career.",

        "Why are you interested in this career path?",

        "Describe a challenging problem you faced while learning or building a project.",

        "What is one technical skill you are currently improving?"
    ]

    role_questions = {

        "Software Developer": [

            "Explain the principles of Object-Oriented Programming.",

            "What is the difference between an array and a linked list?",

            "How do you analyze time and space complexity?",

            "Explain a project you have built and its architecture."

        ],

        "AI/ML Engineer": [

            "What is the difference between supervised and unsupervised learning?",

            "What is overfitting and how can it be reduced?",

            "How do you evaluate a machine learning model?",

            "Explain the difference between training, validation and testing data."

        ],

        "Data Analyst": [

            "What is the difference between INNER JOIN and LEFT JOIN?",

            "How do you handle missing data?",

            "How would you explain data insights to a non-technical audience?",

            "What steps would you follow when analyzing a new dataset?"

        ],

        "Frontend Developer": [

            "What is the difference between props and state in React?",

            "How do you make a website responsive?",

            "Explain React hooks.",

            "How do you connect a frontend application to an API?"

        ],

        "Backend Developer": [

            "What is a REST API?",

            "What is the difference between authentication and authorization?",

            "How would you secure an API?",

            "Explain the client-server architecture."

        ],

        "Data Scientist": [

            "What is the difference between precision and recall?",

            "How do you approach a new data science problem?",

            "What is feature engineering?",

            "How do you validate a predictive model?"

        ]

    }

    personalized_questions = []

    if strengths:

        personalized_questions.append(

            f"You listed {strengths[0].title()} as one of your strengths. Explain how you have used it in practice."

        )

    if gaps:

        personalized_questions.append(

            f"You are currently improving {gaps[0].title()}. How are you planning to learn and apply this skill?"

        )

    if projects:

        personalized_questions.append(

            f"Explain the architecture, technologies and challenges involved in your project: {projects[0].title()}."

        )

    return {

        "common": common_questions,

        "technical":
            role_questions.get(role, []),

        "personalized":
            personalized_questions

    }


# ============================================================
# MAIN ANALYSIS FUNCTION
# ============================================================

def analyze_student(data):

    name = data.get(
        "name",
        "Student"
    ).strip()

    education = data.get(
        "education",
        ""
    ).strip()

    goal = data.get(
        "goal",
        ""
    ).strip()

    experience = data.get(
        "experience",
        "Beginner"
    ).strip()

    plan_days = int(
        data.get(
            "plan_days",
            60
        )
    )

    skills = split_items(
        data.get("skills", [])
    )

    interests = split_items(
        data.get("interests", [])
    )

    projects = split_items(
        data.get("projects", [])
    )

    # --------------------------------------------------------
    # Calculate career scores
    # --------------------------------------------------------

    career_scores = []

    role_matches = {}

    for role_name in CAREERS:

        score, matched = calculate_role_score(

            skills,

            interests,

            role_name,

            goal

        )

        career_scores.append({

            "role": role_name,

            "score": score

        })

        role_matches[role_name] = matched

    career_scores.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    # --------------------------------------------------------
    # Determine target role
    # --------------------------------------------------------

    if goal in CAREERS:

        target_role = goal

    else:

        target_role = career_scores[0]["role"]

    # --------------------------------------------------------
    # Skill gap analysis
    # --------------------------------------------------------

    required_skills = CAREERS[
        target_role
    ]["skills"]

    matched = role_matches[
        target_role
    ]

    missing = [

        skill

        for skill in required_skills

        if skill not in skills

    ]

    additional_skills = [

        skill

        for skill in skills

        if skill not in required_skills

    ]

    completion_percent = round(

        len(matched)
        / len(required_skills)
        * 100

    )

    career_match_score = next(

        item["score"]

        for item in career_scores

        if item["role"] == target_role

    )

    # --------------------------------------------------------
    # Generate professional summary
    # --------------------------------------------------------

    professional_summary = generate_professional_summary(

        name,

        education,

        target_role,

        matched,

        missing,

        interests,

        experience

    )

    # --------------------------------------------------------
    # Generate personalized roadmap
    # --------------------------------------------------------

    roadmap = generate_daywise_roadmap(

        missing,

        matched,

        target_role,

        plan_days

    )

    # --------------------------------------------------------
    # Return complete report
    # --------------------------------------------------------

    return {

        "master_profile": {

            "student": name,

            "target_role": target_role,

            "experience_level": experience,

            "career_match_score":
                career_match_score,

            "plan_days": plan_days,

            "strengths": [

                skill.title()

                for skill in matched

            ],

            "skill_gaps": [

                skill.title()

                for skill in missing

            ],

            "additional_skills": [

                skill.title()

                for skill in additional_skills

            ]

        },

        "professional_summary":
            professional_summary,

        "career_scores":
            career_scores,

        "skill_gap": {

            "matched": [

                skill.title()

                for skill in matched

            ],

            "missing": [

                skill.title()

                for skill in missing

            ],

            "completion_percent":
                completion_percent

        },

        "learning_roadmap":
            roadmap,

        "recommended_projects":
            CAREERS[target_role]["projects"],

        "interview_preparation":
            generate_interview_questions(

                target_role,

                matched,

                missing,

                projects

            ),

        "consistency_note":
            "All sections of this report are generated from the same Master Career Profile. The professional summary, skill-gap analysis, day-wise roadmap, project recommendations and interview preparation therefore remain aligned with the student's current skills and selected career goal."

    }