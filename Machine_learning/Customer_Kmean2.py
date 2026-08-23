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
    X = df[["AnnualIncome","spendingScore"]]

    print("Selection features :")
    print(X.head())
    
if __name__ == "__main__":
    main()