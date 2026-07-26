
import sys

def main():

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation script is used to travel the directory")
            print("For better usage plese check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Plese execute the script as ")
            print("Python FileName.py DirectoryName")
            print("Directory name should be absulute path")
        else:
            DirectoryName = sys.argv[1]
            print("Directory name is  :",DirectoryName)

    else: 
        print("Invalid no of arguments")
        print("Plese use --h or --u for more information")

if __name__ == "__main__":
    main()