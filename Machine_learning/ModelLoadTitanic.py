import pandas as pd
import joblib

def LoadModel(filename):
    model = joblib.load(filename)

    print("Model load successfully")

    print(model.feature_names_in_)

    return model

def PerdictPassenger(model):
    print("Enter the information")

    pclass = int(input("Enter Pclass (1/2/3)"))
    Sex = int(input("Enter Sex : (0 - F / 1 : M)"))
    Age = float(input("Enter Age :"))
    sibsp = int(input("Enter sibsp :"))
    Parch = int(input("Enter Parch :"))
    Fare = float(input("Enter Fare :"))
    Embarked = float(input("Enter Embarked : (0/1/2)"))

    passenger = pd.DataFrame([{
        "Passengerid": 1,
        "Age": Age,
        "Fare": Fare,
        "Sex": Sex,
        "sibsp": sibsp,
        "Parch": Parch,
        "zero": 0,
        "Pclass": pclass,
        "Embarked_1.0": 1 if Embarked == 1 else 0,
        "Embarked_2.0": 1 if Embarked == 2 else 0
    }])

    passenger = passenger[model.feature_names_in_]

    result = model.predict(passenger)

    print(result)

def main():
    model = LoadModel("MarvellousTitanic.pkl")

    PerdictPassenger(model)
    
if __name__ == "__main__":
    main()