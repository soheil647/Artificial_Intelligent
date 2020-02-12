import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pulp as p

# from sympy import *
df = pd.read_csv("AdmissionPredict.csv")
print(df)

########################################################################################
# Using Head/Tail Function to see 5 first Rows/2 Last Row of DataFrame
print(df.head(5))
print(df.tail(2))

# Using info to find How many NaN are in each columns
print(df.info())

# Using Describe Function to see info of data frame
print(df.describe())

# Because of info we know which columns have NaN Data
print("GRE Score NaN Number is:", df["GRE Score"].isna().sum())
print("TOEFL NaN Number is:", df["TOEFL Score"].isna().sum())
print("CGPA NaN Number is:", df["CGPA"].isna().sum())

########################################################################################
# Filling Every NaN with its column mean except last column
df = df.fillna(df.loc[:, ["GRE Score", "TOEFL Score", "CGPA"]].mean())
print("DataFrame with NaN Replaced")
print(df)  # to Show NaN are Replaced

########################################################################################
# Uncomment for Plots
# ScatterPlot for Each Variable for Chance of Admit Column
plt.xlabel('Serial No.')
plt.ylabel('Chance of Admit')
plt.plot(df["Serial No."], df["Chance of Admit"], 'bo')
plt.show()

plt.xlabel('GRE Score')
plt.ylabel('Chance of Admit')
plt.plot(df["GRE Score"], df["Chance of Admit"], 'ro')
plt.show()

plt.xlabel('TOEFL Score')
plt.ylabel('Chance of Admit')
plt.plot(df["TOEFL Score"], df["Chance of Admit"], 'go')
plt.show()

plt.xlabel('University Rating')
plt.ylabel('Chance of Admit')
plt.plot(df["University Rating"], df["Chance of Admit"], 'yo')
plt.show()

plt.xlabel('SOP')
plt.ylabel('Chance of Admit')
plt.plot(df["SOP"], df["Chance of Admit"], 'co')
plt.show()

plt.xlabel('LOR ')
plt.ylabel('Chance of Admit')
plt.plot(df["LOR "], df["Chance of Admit"], 'mo')
plt.show()

plt.xlabel('CGPA')
plt.ylabel('Chance of Admit')
plt.plot(df["CGPA"], df["Chance of Admit"], 'ko')
plt.show()

plt.xlabel('Research')
plt.ylabel('Chance of Admit')
plt.plot(df["Research"], df["Chance of Admit"], 'ro')
plt.show()

########################################################################################
# # Filter Accepted Students
FilterAccepted = df[(df['CGPA'] >= 9) & (df['TOEFL Score'] >= 110)]
print("Number of Accepted Students are " + str(FilterAccepted['Serial No.'].count()))  # 97 Students are accepted
#
# # Calculate GRE for each university
for i in range(1, 6):
    x = df.loc[df['University Rating'] == i]['GRE Score'].mean()
    print("University Rate " + str(i) + " Mean GRE is " + str(x))

########################################################################################
df_New = df[["CGPA", "Chance of Admit"]]

