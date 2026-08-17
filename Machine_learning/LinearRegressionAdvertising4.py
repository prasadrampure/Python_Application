import numpy as np
import pandas as pd
import matplotlib.pyplot

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousRegression(DataPath):
    border = "-"*40
    
    # step 1 : Load the data
    print(border)
    print("step 1 : Load the data")
    print(border)

    df = pd.read_csv(DataPath)

    print(df.head())

    # step 2 : Remove unwanted columns
    print(border)
    print("step 2 : Remove unwanted columns")
    print(border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    # step 3 : check Missing values

    print(border)
    print("step 3 : check Missing values")
    print(border)

    print("Total Missing values :")
    print(border)
    print(df.isnull().sum())

    # step 4 : Statistical Summary
    print(border)
    print("step 4 : Statistical Summary")
    print(border)

    print(df.describe())

    # step 5 : Correlation

    print(border)
    print("step 5 : Correlation")
    print(border)

    print(df.corr())
    
def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()