Task_05_Descriptive_Stats
Overview
This project explores the use of descriptive statistics and prompt engineering with large language models (LLMs) such as ChatGPT on a public sports dataset. Specifically, the NCAA Men's College Basketball 2025 dataset (cbb25.csv) is analyzed using Python, and basic natural language questions about the data are asked of ChatGPT to test its accuracy and reasoning.

Repository Structure
Python_script/ — Python scripts and notebooks for data exploration, descriptive statistics, and visualization.

Results/ — Collection of LLM prompts, ChatGPT responses, and notes comparing model answers with ground truth from Python analysis.

visualizations/ — Visualization images generated during exploratory data analysis.

README.md — This file, providing an overview and guide to the project.

Dataset Information
Dataset: NCAA Men’s College Basketball 2025 season (cbb25.csv)

Number of teams: 364

Key columns include: Team, Conference (CONF), Wins (W), Offensive Efficiency (ADJOE), Defensive Efficiency (ADJDE), Effective FG% Offensive (EFG_O), Turnovers (TOR), and others.

Note: The dataset file is NOT included per assignment instructions; please download from Kaggle Dataset Link.

Project Workflow
Data Exploration and Descriptive Statistics

Loaded and examined dataset with pandas.

Computed basic statistics such as team counts, max/min values, averages, and distributions.

Created visualizations including histograms, bar charts, scatter plots, and correlation heatmaps.

Prompt Engineering and LLM Testing

Selected key factual questions about the dataset.

Tested ChatGPT’s ability to answer these questions based on provided data samples.

Recorded and compared ChatGPT’s answers with Python-derived ground truth.

Documented successes, challenges, and observations in prompt testing logs.

Reporting and Reflection

Organized findings and outputs in GitHub repository folders.

Prepared progress updates aligned with assignment deadlines.

Example Questions Tested with ChatGPT
How many teams are in the dataset?

Which team had the most wins?

What is the average number of wins across all teams?

Which conference has the highest number of teams?

Which team has the highest offensive efficiency (ADJOE)?

Which team has the best defensive efficiency (lowest ADJDE)?

ChatGPT answered each of these correctly when provided with a sample of the dataset.

