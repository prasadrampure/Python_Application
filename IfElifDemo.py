
print("please enter your age : ")
Age = int(input())

if(Age <= 5):
    print("Free entry")
elif(Age > 5 and Age <= 18):
    print("Ticket price : 900")
elif(Age > 18 and Age <= 40):
    print("Ticket price : 1200")
else:
    print("Ticket price : 500") 