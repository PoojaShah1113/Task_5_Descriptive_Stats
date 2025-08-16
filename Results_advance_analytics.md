Research Task 06 - Prompt Testing Log
Objective
Evaluate how accurately ChatGPT answers advanced statistical and predictive questions using the NCAA Men’s College Basketball 2025 dataset (cbb25.csv).

Dataset Overview
Number of Teams: 364

Key Columns: Team, Conference (CONF), Wins (W), Offensive Efficiency (ADJOE), Defensive Efficiency (ADJDE), Effective FG% Offensive (EFG_O), Turnovers (TOR), Turnovers Forced (TORD), etc.

Prompt 1: Correlation & Importance

Questions Asked

Which metrics have the highest positive correlation with wins?

Which metrics have the strongest negative correlation with wins?

Based on correlation, is offensive efficiency (ADJOE) or defensive efficiency (ADJDE) more important for winning games?

Python Analysis (Ground Truth)

Positive correlations: WAB (0.863), BARTHAG (0.749), ADJOE (0.682)

Negative correlations: RK (-0.759), ADJDE (-0.682), EFG_D (-0.669)

Importance comparison: Almost equal - ADJOE (+0.682) vs ADJDE (-0.682)

ChatGPT Responses and Accuracy

Positive correlations:  Partially correct - Claimed ADJOE is highest; followed by BARTHAG .

Negative correlations:  Partially correct - Identified ADJDE and EFG_D but omitted RK.

Importance comparison:  Incorrect — Claimed offense slightly more predictive; ground truth shows equal correlation magnitude.

Prompt 2: Regression Impact

Questions Asked
4. Effect on wins for a 1-point increase in offensive efficiency (ADJOE)?
5. Effect on wins for a 1-point improvement in defensive efficiency (ADJDE)?

Python Analysis (Ground Truth)
4. ADJOE: +0.32 wins
5. ADJDE: +0.38 wins (lower is better)

ChatGPT Responses and Accuracy

ADJOE: Reported +0.36 wins.

ADJDE: Reported +0.29 wins.


Prompt 3: Scenario Simulation (Houston)

Questions Asked
9. Predicted wins with current efficiency?
10. Wins with +5 offensive efficiency?
11. Wins with -5 defensive efficiency?

Python Analysis (Ground Truth)
9. Current: 29.86 wins
10. +5 ADJOE: 31.48 wins
11. -5 ADJDE: 31.74 wins

ChatGPT Responses and Accuracy

Current:  Reported 30.9 wins

+5 ADJOE: Reported 32.6 wins

-5 ADJDE: Reported 32.4 wins

Observations and Notes

ChatGPT handled basic interpretations (e.g., defensive stats being negative correlations) reasonably well but frequently misreported exact numerical values.

Missed key top-correlated metrics (e.g., WAB, RK).

Scenario simulations were consistently inflated compared to Python-calculated predictions.

Suggests a pattern: LLM reasoning was directionally correct but quantitatively unreliable without the dataset context.