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