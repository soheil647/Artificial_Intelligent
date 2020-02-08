import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AdmissionPredict.csv")
print(df)

# Using Head/Tail Function to see 5 first Rows/2 Last Row of DataFrame
# print(x.head(5))
# print(x.tail(2))

# Using info to find How many NaN are in each columns
# print(x.info())

# Using Describe Function to see info of data frame
# print(x.describe())

# Because of info we know which columns have NaN Data
print("GRE Score NaN Number is:")
print(df["GRE Score"].isna().sum())
print("TOEFL NaN Number is:")
print(df["TOEFL Score"].isna().sum())
print("CGPA NaN Number is:")
print(df["CGPA"].isna().sum())

# Filling Every NaN with its column mean except last column
df = df.fillna(df.loc[:, ["GRE Score", "TOEFL Score", "CGPA"]].mean())
# print(df)  # to Show NaN are Replaced

# ScatterPlot for Each Variable for Chance of Admit Column
plt.subplot(2 , 1 , 1)
plt.xlabel('')
plt.plot(df["GRE Score"], df["Chance of Admit"], 'bo')
plt.subplot(2, 1, 2)
plt.plot(df["TOEFL Score"], df["Chance of Admit"], 'ro')
plt.show()
plt.plot(df["TOEFL Score"], df["Chance of Admit"], 'ro')
plt.show()

