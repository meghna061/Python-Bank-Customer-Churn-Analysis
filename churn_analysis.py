# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:10:51 2026

@author: Meghna
"""
#For working directory 
import os 
print(os.getcwd())
#For reading excel file 
import pandas as pd
df = pd.read_excel("Data\\Churn_Modelling.xlsx")
#Studying data
print(df.head())
print(df.shape)
print(df.columns)
df.info()
#Checking missing values
df.isnull().sum()
df.describe()
pd.crosstab(df['IsActiveMember'], df['Exited'])
#Checking Duplicate values
df.duplicated().sum()
df_clean=df.drop(['RowNumber','CustomerId','Surname'],axis=1)
print(df.shape)
print(df_clean.shape)
print(df_clean.columns)
df_clean.columns.tolist()
df_clean['Exited'].value_counts()
df_clean['IsActiveMember'].value_counts()
df_clean['Exited'].value_counts(normalize=True)*100
import matplotlib.pyplot as plt
df_clean['Exited'].value_counts().plot(kind='bar')
plt.title('Customer Churn Distribution')
plt.xlabel('Exited')
plt.ylabel('Number of Customers')
plt.get_fignums()

pd.crosstab(df_clean['Geography'], df_clean['Exited'])
print("Geography vs Churn (Counts)")
print(pd.crosstab(df_clean['Geography'], df_clean['Exited']))
print("\nGeography vs Churn (%)")
print(pd.crosstab(
    df_clean['Geography'],
    df_clean['Exited'],
    normalize='index'
) * 100)

print("Gender vs Churn (Counts)")
print(pd.crosstab(df_clean['Gender'], df_clean['Exited']))
print("\nGender vs Churn (%)")
print(pd.crosstab(
    df_clean['Gender'],
    df_clean['Exited'],
    normalize='index'
) * 100)

print("Active Member vs Churn (Counts)")
print(pd.crosstab(df_clean['IsActiveMember'], df_clean['Exited']))
print("\nActive Member vs Churn (%)")
print(pd.crosstab(
    df_clean['IsActiveMember'],
    df_clean['Exited'],
    normalize='index'
) * 100)

print("Credit Card vs Churn (Counts)")
print(pd.crosstab(df_clean['HasCrCard'], df_clean['Exited']))
print("\nCredit Card vs Churn (%)")
print(pd.crosstab(
    df_clean['HasCrCard'],
    df_clean['Exited'],
    normalize='index'
) * 100)

print("Products vs Churn (Counts)")
print(pd.crosstab(df_clean['NumOfProducts'], df_clean['Exited']))
print("\nProducts vs Churn (%)")
print(pd.crosstab(
    df_clean['NumOfProducts'],
    df_clean['Exited'],
    normalize='index'
) * 100)

print("\n" + "="*60)
print("AGE SUMMARY BY CHURN STATUS")
print("="*60)
print(df_clean.groupby('Exited')['Age'].describe().round(2))

print("\n" + "="*60)
print("BALANCE SUMMARY BY CHURN STATUS")
print("="*60)
print(df_clean.groupby('Exited')['Balance'].describe().round(2))

print("\n" + "="*60)
print("CREDIT SCORE SUMMARY BY CHURN STATUS")
print("="*60)
print(df_clean.groupby('Exited')['CreditScore'].describe().round(2))

numerical_cols = [
    'Age',
    'Balance',
    'CreditScore',
    'EstimatedSalary',
    'Tenure'
]

for col in numerical_cols:

    df_clean.boxplot(column=col, by='Exited')

    plt.title(f'{col} by Churn Status')
    plt.suptitle('')
    plt.xlabel('Exited')
    plt.ylabel(col)

    plt.get_fignums()
    
categorical_cols = [
    'Geography',
    'Gender',
    'IsActiveMember',
    'HasCrCard',
    'NumOfProducts',
    'Tenure'
]
for col in categorical_cols:

    (
        pd.crosstab(
            df_clean[col],
            df_clean['Exited'],
            normalize='index'
        ) * 100
    ).plot(kind='bar')

    plt.title(f'{col} vs Churn Rate')
    plt.xlabel(col)
    plt.ylabel('Percentage')

    plt.get_fignums()
    
corr_matrix = df_clean.corr(numeric_only=True)

print(corr_matrix['Exited'].sort_values(ascending=False))

#Correlation 

import seaborn as sns

plt.figure(figsize=(10,8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Correlation Heatmap')
plt.get_fignums()

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# Correlation matrix
corr_matrix = df_clean.corr(numeric_only=True)
# Create mask for upper triangle
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
# Plot heatmap
plt.figure(figsize=(10, 8))

sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,
    cmap='Blues',
    fmt='.2f',
    linewidths=0.5
)
plt.title('Correlation Heatmap')
plt.get_fignums()

import matplotlib.pyplot as plt
import os

# Create folder
os.makedirs("All_Plots", exist_ok=True)

# Save all open figures as PNG
for i in plt.get_fignums():
    fig = plt.figure(i)
    fig.savefig(
        f"All_Plots/Plot_{i}.png",
        dpi=600,
        bbox_inches='tight'
    )

print(f"{len(plt.get_fignums())} plots saved successfully in 'All_Plots' folder!")