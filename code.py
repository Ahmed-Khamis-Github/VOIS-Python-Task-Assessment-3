import pandas as pd
import numpy as np

df = pd.read_csv("Employees.csv")
df = df.drop_duplicates()
df["Age"] = np.floor(df["Age"])

df["Salary(EGP)"] = df["Salary(USD)"] * 48

print("Average Age:", df["Age"].mean())
print("Median Salary in EGP:", df["Salary(EGP)"].median())
print("Ratio between Males and Females:", len(df[df["Gender"] == "M"]) / len(df[df["Gender"] == "F"]))

df.to_csv("new_file.csv")