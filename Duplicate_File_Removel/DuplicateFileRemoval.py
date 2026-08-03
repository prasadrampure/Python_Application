import os
import sys
import schedule
import hashlib
import time
import smtplib
from email.message import EmailMessage

def CalculateChkSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def DeleteDuplicate(DirectoryPath):

    Ret = False

    Ret = os.path.exists(DirectoryPath)
    Duplicate = dict()

    if (Ret == False):
        print("Marvellous Automation error : There is no such directory with name",DirectoryPath)
        return

    Ret = os.path.isdir(DirectoryPath)

    if(Ret == False):
        print("Marvellous Automation error : It is not a directory with name",DirectoryPath)
        return

    timestamp = time.strftime("%d-%m-%Y_%H-%M-%S")
    FileName = os.path.join(DirectoryPath,f"Filelog_{timestamp}.log")

  

    for FolderName,SubFolder,Files in os.walk(DirectoryPath):
        for fname in Files:
            fname = os.path.join(FolderName,fname)

            Checksum = CalculateChkSum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    logF = open(FileName,"a")
    logF.write("-"*100+"\n")
    logF.write("DUPLICATE FILES REMOVAL LOG"+"\n")
    logF.write("-"*100+"\n")
    logF.write(f"\n Log file created at :{time.ctime()}")
    logF.write("\n\n\n")
    logF.write("-"*100+"\n")
    logF.write("DUPLICATE FILES :-\n")

    for Checksum in Duplicate:
        if len(Duplicate[Checksum]) > 1:
            logF.write("-"*100+"\n")
            logF.write(f"Check Sum Value : {Checksum}\n")
            value = Duplicate.get(Checksum)
            logF.write(f"FileName Associated with : {value}\n")
            logF.write("-"*100+"\n")

    total_files = 0
    for Files in Duplicate.values():
        total_files += len(Files)

    logF.write("-"*100+"\n")
    logF.write("Deleted files:-\n")
    logF.write("-"*100+"\n")

    total_Duplicate = 0
    for Files in Duplicate.values():
        if len(Files) > 1:
            total_Duplicate += len(Files) - 1

    total_DuplicateFilesDeleted = 0
    for Checksum in Duplicate:
        if len(Duplicate[Checksum]) > 1:
            for DuplicateFile in Duplicate[Checksum][1:]:
                total_DuplicateFilesDeleted += 1
                logF.write(f"CheckSum :{Checksum}\n")
                logF.write(f"Deted files:{DuplicateFile}\n")
                os.remove(DuplicateFile)

                logF.write("-"*100+"\n")
    logF.write("END OF LOG FILE")
    logF.write("-"*100+"\n")
    logF.close()

    fobj = open("MailBody.txt","w")
    fobj.write("Jay Ganesh\n")

    fobj.write("The Duplicate file remove has been completed succesfully")
    fobj.write(f"starting time:{time.ctime()}\n")
    fobj.write(f"\n\nTotal files Scanned:{total_files}\n")
    fobj.write(f"Total Duplicate files :{total_Duplicate}\n")
    fobj.write(f"Total Deleted duplicate files:{total_DuplicateFilesDeleted}\n")
    fobj.write(f"Time of Deletion: {time.ctime()}\n")
    fobj.close()

    MailFileReciver(FileName, sys.argv[2])

def MailFileReciver(FileName, reciver):

    mail = EmailMessage()
    mail["From"] = "File Survillence System"
    mail["To"] = reciver
    mail["Subject"] = (f"file Deletion of log file : {time.ctime()}")
    objbody = open("MailBody.txt","r")
    body = objbody.read()

    mail.set_content(body)

    attachment = open(FileName,"rb")
    data = attachment.read()
    name = attachment.name

    mail.add_attachment(data,maintype="text",subtype="plain",filename= name)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    smtp.login("@gmail","Password")
    smtp.send_message(mail)
    print("Mail sent Succesfully")
    smtp.quit()

def main():
    Border = ("-"*50)
    print(Border)
    print("Duplicate file removal Automation Script started")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("It Identifies duplicate files")
            print("Also Deletes Duplicate files")
            print("It generates Detail Log file")
            print("It sends the file thrugh Email")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Plese execute the script as ")
            print("Python FileName.py")

    elif len(sys.argv) == 3:
        schedule.every(1).minutes.do(DeleteDuplicate,sys.argv[1])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invaid number of arguments")
        print("Please use --h or --u for more information")

    print(Border)
    print("Thank you for using automation script")
    print(Border)

if __name__ == "__main__":
    main()