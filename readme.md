🏀 Task_05_Descriptive_Stats
Overview
This project explores descriptive statistics and prompt engineering with large language models (LLMs) such as ChatGPT using a public sports dataset.
The dataset analyzed is the NCAA Men's College Basketball 2025 season (cbb25.csv).

The main objective was to:

Perform data exploration and compute descriptive statistics using Python.

Test ChatGPT’s ability to answer natural language questions about the dataset.

📂 Repository Structure
bash
Copy
Edit
Task_05_Descriptive_Stats/
│
├── Python_script/       # Python scripts and notebooks for data exploration & visualization
├── Results/             # LLM prompts, ChatGPT responses, and comparison notes
├── visualizations/      # Generated plots and charts (EDA visuals)
└── README.md            # Project documentation
📊 Dataset Information
Dataset: NCAA Men’s College Basketball 2025 season (cbb25.csv)

Teams: 364

Key Columns:

Team

CONF – Conference

W – Wins

ADJOE – Offensive Efficiency

ADJDE – Defensive Efficiency

EFG_O – Offensive Effective FG%

TOR – Turnovers

… and other advanced stats

Note: Dataset file is NOT included in this repository as per assignment instructions. Please download from Kaggle.

🔄 Project Workflow
1. Data Exploration & Descriptive Stats
Loaded and examined dataset with pandas

Computed:

Team counts

Max/Min values

Averages & distributions

Generated visualizations: histograms, bar charts, scatter plots, heatmaps

2. Prompt Engineering & LLM Testing
Selected factual, dataset-based questions

Tested ChatGPT’s reasoning and accuracy

Compared ChatGPT’s answers to Python-derived results

3. Reporting & Reflection
Organized results and prompts in dedicated folders

Documented observations and success/failure cases

❓ Example Questions Tested with ChatGPT
How many teams are in the dataset?

Which team had the most wins?

What is the average number of wins across all teams?

Which conference has the highest number of teams?

Which team has the highest offensive efficiency (ADJOE)?

Which team has the best defensive efficiency (lowest ADJDE)?

Observation:
ChatGPT answered these correctly when provided with an appropriate dataset sample.

🚀 Key Learnings
Prompt clarity significantly impacts LLM accuracy.

Combining Python-based analytics with LLM reasoning enables fast insights and cross-verification.
