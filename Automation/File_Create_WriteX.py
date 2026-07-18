def main():
    try:
        fobj = open("Demo.txt","w")
        print("File gets opened")

        fobj.write("Marvellous infosystems")
        

        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present current directory")

if __name__ == "__main__":
    main()