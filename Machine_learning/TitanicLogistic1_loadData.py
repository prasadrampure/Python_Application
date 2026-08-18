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

#---------------------------------------------------
#  Function Name : main
#  Description : entry point function
#  Input :       none
#  Output :      none
#  Author :      Prasad Rampure
#  Date  :       16/08/2026
#---------------------------------------------------
def main():
    LoadData("MarvellousTitanicDataset.csv")
    
if __name__ == "__main__":
    main()