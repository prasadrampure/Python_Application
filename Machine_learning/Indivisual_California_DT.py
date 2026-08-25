import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Step 1 : Load the data

df = pd.read_csv("california_housing.csv")

print("Shape of Dataser :",df.shape)
print("First 5 records :",df.head())

# Step 2 : Separate Features & Labels

X = df.drop("target",axis=1)
Y = df["target"]

print("Shape of X :",X.shape)
print("Shape of Y :",Y.shape)

# Step 3 : Split the Dataset for Training & Testing

x_train,x_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42)

print("spliting successfully")

# Step 4 : Create the model

model = DecisionTreeRegressor(random_state=42)

# Step 5 : Train the model

model = model.fit(x_train,Y_train)
print("model traning successfully")

# Step 6 : Test the model

Y_pred = model.predict(x_test)
print("Testing the model successfully")

# Step 7 : Evaluate the model

print("MSE :",mean_squared_error(Y_test,Y_pred))
print("R2 :",r2_score(Y_test,Y_pred))