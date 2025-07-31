# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load Dataset (change the path if your CSV is in a different location)
df = pd.read_csv('cbb25.csv')

# 3. Preview Data
print("First 5 rows of data:")
print(df.head())
print("\nColumn names:")
print(list(df.columns))

# 4. Basic Descriptive Statistics
print("\nSummary statistics (all numeric columns):")
print(df.describe())

print("\nNumber of teams in the dataset:", len(df))

print("\nList of conferences and how many teams per conference:")
print(df['CONF'].value_counts())

print("\nTeam with the most wins:")
most_wins = df[df['W'] == df['W'].max()]
print(most_wins[['Team', 'CONF', 'W']])

print("\nAverage number of wins:")
print(round(df['W'].mean(), 2))

print("\nTeam with highest Offensive Efficiency (ADJOE):")
best_offense = df[df['ADJOE'] == df['ADJOE'].max()]
print(best_offense[['Team', 'CONF', 'ADJOE']])

print("\nTeam with highest Defensive Efficiency (lowest ADJDE):")
best_defense = df[df['ADJDE'] == df['ADJDE'].min()]
print(best_defense[['Team', 'CONF', 'ADJDE']])

# 5. Example Calculation: Top 10 Teams by Wins
top10 = df.nlargest(10, 'W')[['Team', 'CONF', 'W', 'ADJOE', 'ADJDE']]
print("\nTop 10 teams by wins:")
print(top10)

# 6. Visualizations

# Histogram: Wins Distribution
plt.figure(figsize=(8,4))
plt.hist(df['W'], bins=20, color='cornflowerblue', edgecolor='black')
plt.title('Distribution of Wins')
plt.xlabel('Number of Wins')
plt.ylabel('Number of Teams')
plt.tight_layout()
plt.show()

# Bar chart: Top 10 Teams by Wins
plt.figure(figsize=(10,5))
sns.barplot(data=top10, x='Team', y='W', palette='viridis')
plt.title('Top 10 Teams by Wins')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Number of Wins')
plt.tight_layout()
plt.show()

# Scatter plot: Offensive vs Defensive Efficiency
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='ADJOE', y='ADJDE', hue='W', size='W', palette='coolwarm', legend=False)
plt.title('Offensive vs Defensive Efficiency (size = wins)')
plt.xlabel('Offensive Efficiency (ADJOE)')
plt.ylabel('Defensive Efficiency (ADJDE)')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='Spectral')
plt.title('Correlation Matrix of Key Stats')
plt.tight_layout()
plt.show()
