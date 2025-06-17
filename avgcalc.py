import pandas as pd

# Load CSV file
df = pd.read_csv('data.csv')

# Calculate average of the 'Scores' column
average_score = df['Scores'].mean()

print(f"The average score is: {average_score:.2f}")
