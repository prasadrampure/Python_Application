import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score , confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

# step 1 : Load the Dataset

df = pd.read_csv("breast_cancer.csv")

print("Shape of Dataset :", df.shape)

print("Frist 5 records :")
print(df.head())

# step 2 : Separate features & labels

X = df.drop("target", axis=1)
Y = df["target"]

print("X shape :",X.shape)
print("Y shape :",Y.shape)

# step 3 : Split dataset for training & testing

X_train,X_test,Y_train,Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42)

# step 4 : Scale the features

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.fit_transform(X_test)

# step 5.1 : Crate the Indivisual models

model_log = LogisticRegression(max_iter=1000)

model_det = DecisionTreeClassifier(random_state=42)

model_knn = KNeighborsClassifier(n_neighbors=5)

# step 5.2 : Crate the Voting model

model = VotingClassifier(
    estimators=[
        ("logistic",model_log),
        ("decision_tree",model_det),
        ("knn",model_knn)
    ],
    voting="soft"
)

# step 6 : train the model

model = model.fit(X_train,Y_train)

# step 7 : test the model

y_pred = model.predict(X_test)

# step 8 : Evaluate the model

print("Accuracy :",accuracy_score(Y_test,y_pred))

print("Confusion martrix :")
print(confusion_matrix(Y_test,y_pred))
