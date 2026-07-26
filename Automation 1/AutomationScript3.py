
import sys

def main():

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("Help")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage")
        else:
            DirectoryName = sys.argv[1]
            print("Directory name is  :",DirectoryName)

    else: 
        print("Invalid no of arguments")
        print("Plese use --h or --u for more information")

if __name__ == "__main__":
    main()