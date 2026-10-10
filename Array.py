def CountEvenArray():

    Arr = list(map(int, input("Enter Array Elements :").split()))

    
    count = 0

    for i in Arr:
        if i % 2 == 0:
            count += 1

    print("Count Of Even Numbers :",count)

def main():
    CountEvenArray()

if __name__ == "__main__":
    main()