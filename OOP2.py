class Demo:
    #class variables
    Value1 = 10
    Value2 = 20

    def __init__(self):
        self.No1 = 11
        self.No2 = 21
    # instance method
    def Fun(self):
        print("Inside instance method named as Fun")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)

#object created
dobj = Demo()
dobj.Fun()
