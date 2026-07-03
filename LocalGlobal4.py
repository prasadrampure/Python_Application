no = 11          

def Display():
    global no
    no = 21
    print("From display : ",no)

    
print("Before : ",no)
Display()
print("After :",no)