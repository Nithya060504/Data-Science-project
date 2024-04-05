import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset (you can download it from the provided link)
data = pd.read_csv('case_time_series.csv')

# Extract relevant columns
Y = data.iloc[61:, 1].values  # Daily Confirmed cases
R = data.iloc[61:, 3].values  # Daily Recovered cases
D = data.iloc[61:, 5].values  # Daily Deceased cases
X = data.iloc[61:, 0]         # Dates

# Create a bar chart
plt.figure(figsize=(12, 6))  # Set figure size
plt.bar(X, Y, label='Confirmed Cases', color='b', alpha=0.7)
plt.bar(X, R, label='Recovered Cases', color='g', alpha=0.7)
plt.bar(X, D, label='Deceased Cases', color='r', alpha=0.7)
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('COVID-19 Cases in India (Daily Confirmed, Recovered, and Deceased)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()  # Adjust spacing
plt.show()
