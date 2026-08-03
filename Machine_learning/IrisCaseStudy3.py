from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris Classification Case Study")
    print("-"*30)

    Dataset = load_iris()

    # MetaData of the dataset
    print("Independent Variabels are :")
    print(Dataset.feature_names)
    print("Lenght of Independent variabels :",len(Dataset.feature_names))

    print("Dependent Variabels are :")
    print(Dataset.target_names)
    print("Lenght of dependent variabels :",len(Dataset.target_names))

if __name__ == "__main__":
    main()