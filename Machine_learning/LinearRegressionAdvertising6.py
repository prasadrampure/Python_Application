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

    # step 6 : Separete

    print(border)
    print("step 6 : Separate Independent and Dependent variables")
    print(border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent Variabel :")
    print(X.head())

    print("Dependent variables :")
    print(Y.head())

    # step 7 : Split the dataset

    print(border)
    print("step 7 : Split the dataset")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Training Data :",X_train.shape)
    print("Testing Data :",X_test.shape)
    
def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()