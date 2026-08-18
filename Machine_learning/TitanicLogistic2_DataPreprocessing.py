import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

# step 1 :Load Data
#---------------------------------------------------
#  Function Name : LoadData
#  Description : Load the datafrom CSV
#  Input :       Name of csv file
#  Output :      Data frame
#  Author :      Prasad Rampure
#  Date  :       16/08/2026
#---------------------------------------------------
def LoadData(filename):
    df = pd.read_csv(filename)

    print("Dataset loaded successfully")
    print(df.head())

    return df

# step 2 : Data Preprocessing
#---------------------------------------------------
#  Function Name : PreprocessData
#  Description : it performs data analysis
#  Input :       Data frame
#  Output :      updated Data frame
#  Author :      Prasad Rampure
#  Date  :       16/08/2026
#---------------------------------------------------

def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero"
    ],
    axis = 1, errors = "ignore"
    )

    # Handle missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    #Convert categorical to numeric data
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )
    print(df.head())

    print("Data Preprocessing completed")
    return df 

#---------------------------------------------------
#  Function Name : main
#  Description : entry point function
#  Input :       none
#  Output :      none
#  Author :      Prasad Rampure
#  Date  :       16/08/2026
#---------------------------------------------------
def main():
    # step 1
    df = LoadData("MarvellousTitanicDataset.csv")

    # step 2
    df = PreprocessData(df)
if __name__ == "__main__":
    main()