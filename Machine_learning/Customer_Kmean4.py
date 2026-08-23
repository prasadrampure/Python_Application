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

    # step 3 : Scale the data
    scalar = StandardScaler()

    X_scaled = scalar.fit_transform(X)

    print("Scaled Data :")
    print(X_scaled[:5])

    # step 4 : Elbow method
    WCSS = []

    for k in range(1,11):
        model = KMeans(
            n_clusters= k,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)

        WCSS.append(model.inertia_)

    print("Values of WCSS :")
    for i in range(len(WCSS)):
        print(f"{i+1} : {WCSS[i]}")
    
if __name__ == "__main__":
    main()