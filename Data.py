import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Cleaning And Data Aggrigation
# Checking Null Values 
#print(df.isnull().sum())

# Shape 
#print(df.shape)

# For Information
#rint(df.info())

# Visualize attrition
sns.countplot(data=df, x='Attrition', palette='Set2')
plt.title('Attrition Count')
plt.show()


# Univariate Analysis 
# Attrition Count
sns.countplot(x='Attrition', data=df, palette='Set2')
plt.title("Employee Attrition Count")
plt.show()

# Distribution of Monthly Income
sns.histplot(df['MonthlyIncome'], kde=True)
plt.title("Distribution of Monthly Income")
plt.show()

# Bivariate Analysis
# Attrition vs Job Role
plt.figure(figsize=(10,6))
sns.countplot(x='JobRole', hue='Attrition', data=df)
plt.title("Attrition by Job Role")
plt.xticks(rotation=45)
plt.show()

# Attrition by Age
sns.boxplot(x='Attrition', y='Age', data=df)
plt.title("Attrition by Age")
plt.show()

#Correlation Heatmap
# Select numerical columns
num_cols = df.select_dtypes(include='number')

# Correlation matrix
plt.figure(figsize=(12,10))
sns.heatmap(num_cols.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# JobRole vs Attrition
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='JobRole', hue='Attrition', palette='Set2')
plt.title('Attrition by Job Role')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Department vs Attrition
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Department', hue='Attrition', palette='Set1')
plt.title('Attrition by Department')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# EducationField vs Attrition
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='EducationField', hue='Attrition', palette='Set3')
plt.title('Attrition by Education Field')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#JobSatisfaction vs Attrition
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='JobSatisfaction', hue='Attrition', palette='viridis')
plt.title('Attrition by Job Satisfaction Level')
plt.tight_layout()
plt.show()





print(df.head())