import math
import numpy as np

def MarvellousEucDistance(P1, P2):
    Ans = math.sqrt((P1["X"] - P2["X"])**2  + (P1["Y"] - P2["Y"])**2)
    return Ans

def MarvellousKNNClassifier():
    border = "-"*30

    Data = [
        {"point" : "A", "X" : 1, "Y" : 2, "label" : "Red"},
        {"point" : "B", "X" : 2, "Y" : 3, "label" : "Red"},
        {"point" : "C", "X" : 3, "Y" : 1, "label" : "Blue"},
        {"point" : "D", "X" : 5, "Y" : 6, "label" : "Blue"}
    ]

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    for i in  Data:
        print(i)

    print(border)

    new_point = {"X" : 3, "Y" : 3}

    print("Distances of all points :")
    print(border)

    for d in Data:
        d["distance"] = MarvellousEucDistance(d,new_point)

    for d in Data:
        print(d)
        
    print(border)

    sorted_data = sorted(Data, key = lambda item : item["distance"])

    print(border)
    print("Sorted Data :")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    k = 3

    nearest = sorted_data[:k]

    print(border)
    print("Nearest 3 members are :")
    print(border)

    for d in nearest:
        print(d)

    print(border)

def main():
    MarvellousKNNClassifier()

if __name__ == "__main__":
    main()