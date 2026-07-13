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

    @classmethod
    def Gun(cls):
        print("Inside Class method named as Gun")
        #print(Demo.No1)  Not allowed
        #print(Demo.No2)  Not allowed
        print(Demo.Value1)
        print(Demo.Value2)

#call without object
Demo.Gun()
