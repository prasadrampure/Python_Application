def ChkDivisible():
    No = int(input("Enter The Number :"))

    if No % 3 == 0 and No % 5 == 0:
        return True
    else:
        return False
    
def main():
    Ret = ChkDivisible()
    if Ret == True:
        print("Number is Divisible by 3 & 5")
    else:
        print("Number is Not Divisible by 3 & 5")

if __name__ == "__main__":
    main()