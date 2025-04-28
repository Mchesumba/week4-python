# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Step 2: Load the Dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Step 3: Explore the Dataset
print("\nFirst 5 rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# Step 4: Clean the Dataset (if needed)
# (Iris dataset has no missing values)

# Step 5: Basic Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Grouping by Species and computing the mean
print("\nMean values grouped by species:")
grouped_means = df.groupby('target').mean()
print(grouped_means)

# Step 6: Data Visualization

# 6.1 Line Chart: Sepal length over samples
plt.figure(figsize=(10, 6))
plt.plot(df['sepal length (cm)'])
plt.title('Sepal Length Over Samples')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.grid(True)
plt.show()

# 6.2 Bar Chart: Average Sepal Width per Species
plt.figure(figsize=(8, 6))
sns.barplot(x='target', y='sepal width (cm)', data=df, ci=None)
plt.title('Average Sepal Width per Species')
plt.xlabel('Species')
plt.ylabel('Sepal Width (cm)')
plt.show()

# 6.3 Histogram: Distribution of Petal Length
plt.figure(figsize=(8, 6))
plt.hist(df['petal length (cm)'], bins=20, color='purple')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 6.4 Scatter Plot: Sepal Length vs Petal Length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='target', data=df)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()

# Step 7: Findings/Observations
print("\nFindings:")
print("- Sepal length tends to increase across samples.")
print("- Species have different average sepal widths.")
print("- Petal length shows a clear distribution pattern.")
print("- There is a positive correlation between sepal length and petal length.")
