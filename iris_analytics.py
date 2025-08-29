# Assignment: Analyzing Data with Pandas & Matplotlib
# Dataset I have used is  Iris Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# better looks for the plots
sns.set(style="whitegrid", palette="muted")

# Loading and Exploring the Dataset
iris_data = load_iris(as_frame=True)
df = iris_data.frame

print("First five rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing values per column:")
print(df.isnull().sum())

# for a clean dataset this drops any missing values if there are any 
df = df.dropna()

# Mapping target numbers to species names
df["species"] = df["target"].map(dict(zip(range(3), iris_data.target_names)))

# Data Analysis
print("\nBasic Statistics:")
print(df.describe())

# Grouping: Mean of numerical values per species
grouped = df.groupby("species").mean()
print("\nMean values by species:")
print(grouped)

# Data Visualization

# 1. Line Chart for trends
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Sepal vs Petal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Length (cm)")
plt.legend()
plt.savefig("line_chart.png")  # save plot
plt.show()

# 2. Bar Chart for Category Comparison
plt.figure(figsize=(6,4))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.savefig("bar_chart.png")
plt.show()

# 3. Histogram for Distribution
plt.figure(figsize=(6,4))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# 4. Scatter Plot for Relationship
plt.figure(figsize=(6,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.savefig("scatter_plot.png")
plt.show()

# Findings & Observations
print("\n--- Findings & Observations ---")
print("1. The dataset has no missing values and is clean.")
print("2. Setosa flowers tend to have shorter petal lengths compared to Versicolor and Virginica.")
print("3. Sepal width distribution is roughly normal but varies across species.")
print("4. There is a positive correlation between sepal length and petal length — larger sepals generally mean larger petals.")
