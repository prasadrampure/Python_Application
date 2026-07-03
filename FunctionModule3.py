from Marvellous import Addition
 

def main():
    print("Enter first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())
    
    Ret = Addition(value1, value2) 

    print("Addition is : ",Ret)

    Ret = Substraction(value1, value2) #error

    print("Substraction is : ",Ret)
    
if  __name__ == "__main__":
    main()