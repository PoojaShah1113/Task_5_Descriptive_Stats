# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# 2. Load Dataset
df = pd.read_csv('cbb25.csv')

# 3. Correlation of all metrics with Wins
corr_wins = df.corr(numeric_only=True)['W'].sort_values(ascending=False)
print("\nCorrelation of features with Wins:")
print(corr_wins)

# 4. Offensive vs Defensive Impact
# Regression to see relative impact of ADJOE and ADJDE on Wins
X = df[['ADJOE', 'ADJDE']]
y = df['W']
model = LinearRegression()
model.fit(X, y)
print("\nRegression Coefficients (Impact on Wins):")
print(f"Offensive Efficiency (ADJOE): {model.coef_[0]:.2f}")
print(f"Defensive Efficiency (ADJDE): {model.coef_[1]:.2f} (negative means better defense helps)")

# 5. Identify 'Most Improved Potential' teams
# We'll define potential as teams whose metrics predict more wins than they actually got
df['pred_wins'] = model.predict(X)
df['improvement_gap'] = df['pred_wins'] - df['W']
most_potential = df.sort_values(by='improvement_gap', ascending=False).head(5)
print("\nTeams with the biggest potential improvement based on metrics:")
print(most_potential[['Team', 'CONF', 'W', 'pred_wins', 'improvement_gap']])

# 6. Offensive vs Defensive Tradeoff Plot
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='ADJOE', y='ADJDE', hue='W', palette='coolwarm', size='W', sizes=(50, 300))
plt.title('Offensive vs Defensive Efficiency (color/size = Wins)')
plt.xlabel('Offensive Efficiency (ADJOE)')
plt.ylabel('Defensive Efficiency (ADJDE)')
plt.gca().invert_yaxis()  # lower ADJDE is better
plt.tight_layout()
plt.show()

# 7. Top metrics driving wins (excluding W itself)
plt.figure(figsize=(8,6))
corr_wins.drop('W').head(10).plot(kind='barh', color='teal')
plt.title('Top 10 Factors Correlated with Wins')
plt.xlabel('Correlation with Wins')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# 8. Simulation: Effect of improving ADJOE or ADJDE by 5 points
team_name = "Houston"
team = df[df['Team'] == team_name].iloc[0]
current_pred = model.predict([[team['ADJOE'], team['ADJDE']]])[0]
offense_boost = model.predict([[team['ADJOE'] + 5, team['ADJDE']]])[0]
defense_boost = model.predict([[team['ADJOE'], team['ADJDE'] - 5]])[0]
print(f"\nSimulation for {team_name}:")
print(f"Current Predicted Wins: {current_pred:.2f}")
print(f"With +5 Offensive Efficiency: {offense_boost:.2f} wins")
print(f"With -5 Defensive Efficiency (better defense): {defense_boost:.2f} wins")
