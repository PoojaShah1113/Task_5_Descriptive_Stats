Research Task 05 – Prompt Testing Log
Objective
Evaluate how accurately ChatGPT answers basic statistical questions using the NCAA Men’s College Basketball 2025 dataset (cbb25.csv).

Dataset Overview
Number of Teams: 364

Key Columns: Team, Conference (CONF), Wins (W), Offensive Efficiency (ADJOE), Defensive Efficiency (ADJDE), Effective FG% Offensive (EFG_O), Turnovers (TOR), Turnovers Forced (TORD), etc.

Prompt 1: Basic Descriptive Stats
Questions Asked
How many teams are in the dataset?

Which team had the most wins?

What is the average number of wins across all teams?

Which conference has the highest number of teams?

Which team has the highest offensive efficiency (ADJOE)?

Which team has the best defensive efficiency (lowest ADJDE)?

Python Analysis (Ground Truth)
Total teams: 364

Most wins: Duke (31 wins)

Average wins: 16.93

Largest conference: Big Ten (B10) with 18 teams

Highest offensive efficiency: Auburn (129.0)

Best defensive efficiency: Houston (88.0)

ChatGPT Responses and Accuracy
Teams count: 364 ✅

Most wins: Duke (31 wins) ✅

Average wins: 16.93 ✅

Largest conference: Big Ten (B10) with 18 teams ✅

Highest offensive efficiency: Auburn (129.0) ✅

Best defensive efficiency: Houston (88.0) ✅

Observations and Notes
ChatGPT provided fully correct answers for all straightforward statistical queries.

Demonstrated good understanding of dataset structure and numeric values.

Tested on sample data subset for context, ensuring accurate responses.

Next steps: Explore complex analytic prompts and note any reasoning limitations.