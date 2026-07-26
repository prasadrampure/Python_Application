import sys

def main():

    if(len(sys.argv) == 2):
        DirectoryName = sys.argv[1]
        print("Directory name is  :",DirectoryName)

    else:
    
        print("Invalid no of arguments")

    

if __name__ == "__main__":
    main()