import pandas as pd

Border = "-"*30

#############################
# Step 1 : Load the data set
#############################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded succesfully")
print("Inicial entries from dataset are :")
print(df.head())

################################
# Step 2 : Data Analysis (EDA)
################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape od dataset :",df.shape)

print("Column names :",list(df.columns))

print("Mising values per column :")
print(df.isnull().sum())

print("Class distribution (species count)")
print(df["species"].value_counts())

print("Statistical report of dataset")
print(df.describe())

##################################################
# Step 3 : Deside Independent & Dependent variabels
##################################################

print(Border)
print("Step 3 : Deside Independent & Dependent variabels")
print(Border)

# X : Independent Variable / features
# Y : Dependent Variable / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]

X = df[feature_cols]
Y = df["species"]

print("X Shape :",X.shape)
print("Y Shape :",Y.shape)