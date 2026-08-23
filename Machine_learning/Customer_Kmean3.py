import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    # step 1 : Load The Data
    df = pd.read_csv("Mall_Customers.csv")

    print("Dataset loaded with values")
    print(df.head())

    print("Missing Values :")
    print(df.isnull().sum())

    # step 2 : Feature Selection
    X = df[["AnnualIncome","SpendingScore"]]

    print("Selection features :")
    print(X.head())

    # step 3 : Scale the Data
    scalar = StandardScaler()

    X_scaled = scalar.fit_transform(X)

    print("Scaled Data :")
    print(X_scaled[:5])
    
if __name__ == "__main__":
    main()