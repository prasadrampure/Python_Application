#------------------------------------
#  Deep Learning Pipeline
# ----------------------------------
# 1.  Read the data from csv
# 2.  Data Analysis (EDA)
# 3.  Proprocessing
# 4.  Train Test Split
# 5   Feature Scaling
# 6.  FNN Model traning
# 7.  Model Evaluation
# 8.  Graphicel Representation
# 9.  Model Preserve
# 10. Model loading and preserve
# 11. Test unseen data
#------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score , confusion_matrix

#------------------------------------
# 1.  Read the data from csv
#------------------------------------

print(" 1. Read the data from csv")

data = pd.read_csv("placement_data.csv")

print("Completa Ddataset :")
print(data)

#------------------------------------
# 2.  Data Analysis (EDA)
#------------------------------------

print("2. Data Analysis (EDA)")

print("First 5 rows :")
print(data.head())

print("Column names :")
print(data.columns)

print("Shape Of Dataset :")
print(data.shape)

print("Statistical Summary :")
print(data.describe())

#------------------------------------
# 3. Proprocessing
#------------------------------------

print("3. Proprocessing")

X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = data['Placed']

print("Input Features :")
print(X.head())

print("Target :")
print(Y.head())

#------------------------------------
# 4. Train Test Split
#------------------------------------

print("4. Train Test Split")

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.30,
    random_state=42
)

print("Training Input Shape :",X_train.shape)
print("Testing Input Shape :",X_test.shape)
print("Training Output Shape :",Y_train.shape)
print("Testing Output Shape :",Y_test.shape)

#------------------------------------
# 5. Feature Scaling
#------------------------------------

print("5. Feature Scaling")

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

print("Sclaed Traning Data :")
print(X_train_scaled[:5])

#------------------------------------
# 6. FNN Model traning
#------------------------------------

print("6. FNN Model traning")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print(model)

print("Train the Model")

model.fit(X_train_scaled,Y_train)

print('Model teaining completed')

#------------------------------------
# 7. Model Evaluation
#------------------------------------

print("7. Model Evaluation")

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy is :",accuracy)

cm = confusion_matrix(Y_test,Y_pred)
print("Confision Matrix :",cm)

print("Predict the probablity :")

Y_prob = model.predict_proba(X_test_scaled)

print(Y_prob[:5])

#------------------------------------
# 9. Model Preserve
#------------------------------------

print("9. Model Preserve")

joblib.dump(model,"placement_fnn_model.pkl")
joblib.dump(scalar,"placement_scalar.pkl")

print("Model and scaler getsdump successfully")

#------------------------------------
# 10. Model loading and preserve
#------------------------------------

print("10. Model loading and preserve")

loaded_model = joblib.load("placement_fnn_model.pkl")
loaded_scalar = joblib.load("placement_scalar.pkl")

print("Model Gets Loaded seccessfully")

#------------------------------------
# 11. Test unseen data
#------------------------------------

new_student = pd.DataFrame([[70,75,80,85,1]], columns =['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scalar.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)

new_probablity = loaded_model.predict_proba(new_student_scaled)

print("New Students Data :")
print(new_student)

print("Prediction probablity :",new_probablity)

if new_prediction[0] == 1:
    print("Prediction : Placed")
else:
    print("Prediction : Not Placed")