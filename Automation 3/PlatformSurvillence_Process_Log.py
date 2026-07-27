import psutil
import sys
import os
import time
import schedule

def ProcessScan():
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_persent"] = proc.memory_percent()

        print("--------------------------------------------")
        print(info)
        print("--------------------------------------------")

def PlatformSurvillence(FolderName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)
    
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is existsting but its not a directory")
            return
        
    else:
        os.mkdir(FolderName)
        print("Directory for the log gets created succesfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log file gets succesfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("----- Marvellous Platform Survillence System -----\n")
    fobj.write("Log file gets created at : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("-------- System Report ---------\n")

    # CPU information
    fobj.write("Number of activate CPU core : %s \n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    # RAM information
    memory = psutil.virtual_memory()

    fobj.write("RAM Usage : %s %%\n" %memory.percent)
    fobj.write("Total RAM Avilable : %s \n" %memory.total)
    fobj.write(Border+"\n")

    # Network Usage
    netobj = psutil.net_io_counters()

    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent / (1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")



    fobj.write("\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("--------- End od log file ---------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    ProcessScan()

    Border = "-"*50
    print(Border)
    print("----- Marvellous Platform Survillence System -----")
    print(Border)

    # --h & --u handling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is use to perform")
            print("1 : It fetch the information of running process")
            print("2 : It featch information abount the RAM")
            print("3 : It fetch information about the secondary storage as HDD")
            print("4 : It fetch information abount microprocesor")
            print("5 : it gets auto schedule periodically")
            print("6 : it maintain all records intp log file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")

        else:
            print("Unable to proceed as argument are not matching")
            print("Please use --h or --u flag for getting more details")

    #Actual project code
    elif(len(sys.argv) == 3):

        #print("CPU Usage :",psutil.cpu_percent())
        print("Schedular started succesfully")
        print("Press Ctrl + C to abort the automation script") 

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillence, sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid no of arguments")
        print("Unable to proceed as argument are not matching")
        print("Please use --h or --u flag for getting more details")


    print(Border)
    print("---Thank you for using our automation system --- ")
    print(Border)
 
if __name__ == "__main__":
    main()