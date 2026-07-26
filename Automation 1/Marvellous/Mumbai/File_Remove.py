import os

def main():
    try:
        #fobj.remove() = not applicable
        os.remove("Demo.txt")
        
    except FileNotFoundError as fobj:
        print("File is not present current directory")

if __name__ == "__main__":
    main()