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
    axis = 1,errors = "ignore"
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

# step 3 : split data
#---------------------------------------------------
#  Function Name : Split Data
#  Description : it performs spliting activity
#  Input :       Data frame
#  Output :      4 subset for training and testing
#  Author :      Prasad Rampure
#  Date  :       16/08/2026
#---------------------------------------------------

def SplitData(df):
    X = df.drop("Survived", axis=1)
    Y = df["Survived"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Dataset Spliting completed successfully")
    return X_train,X_test,Y_train,Y_test

# step 4 : train model
#---------------------------------------------------
#  Function Name : Traim model
#  Description : it performs model traning
#  Input :       traning features and labels
#  Output :      trained model
#  Author :      Prasad Rampure
#  Date  :       16/08/2026
#---------------------------------------------------

def TrainModel(X_train,Y_train):
    model = LogisticRegression(max_iter=1000)

    model = model.fit(X_train,Y_train)

    print("Model treained successfully")

    return model

# step 5 : Evaluate model
#---------------------------------------------------
#  Function Name : Evaluate model
#  Description : it performs model esting
#  Input :       model, testing data
#  Output :      none
#  Author :      Prasad Rampure
#  Date  :       16/08/2026
#---------------------------------------------------

def EvaluateModel(model, X_test, Y_test):
    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy :",accuracy)

    print(confusion_matrix(Y_test,Y_pred))

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

    # step 3
    X_train,X_test,Y_train,Y_test = SplitData(df)

    # step 4
    model = TrainModel(X_train,Y_train)

    # step 5
    EvaluateModel(model,X_test,Y_test)
    
if __name__ == "__main__":
    main()