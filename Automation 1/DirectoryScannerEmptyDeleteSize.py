import sys
import os
import time
import schedule

def DirectoryScanner(DirectoryPath = "Marvellous"):
    Border = "-"*40


    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    Ret = False

    Ret = os.path.exists(DirectoryPath)

    if (Ret == False):
        print("Marvellous Automation error : There is no such directory with name",DirectoryPath)
        return

    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation error : It is not a directory with name",DirectoryPath)
        return
        

    print("Log file gets created with name :",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")

    fobj.write("Marvellous automation script \n")

    fobj.write(Border+"\n\n")

    fobj.write("Files from the directory are :\n")

    fobj.write(Border+"\n")

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            fobj.write(fname+"\n")

            print(f"file name {fname} : {os.path.getsize(fname)} bytes")

    fobj.write(Border+"\n")
    fobj.write("Log file gets created at :"+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()

def main():
    Border = "-"*40
    print(Border)
    print("Marvellous automation script")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Automation script is used to travel the directory")
            print("For better usage plese check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Plese execute the script as ")
            print("Python FileName.py DirectoryName")
            print("Directory name should be absulute path")
        else:      
           # schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])
           DirectoryScanner(sys.argv[1])

        #while True:
            #schedule.run_pending()
            #time.sleep(1)
        

    else: 
        print("Invalid no of arguments")
        print("Plese use --h or --u for more information")
    
    print(Border)
    print("Thank you for using marvellous automation script")
    print(Border)
 
if __name__ == "__main__":
    main()