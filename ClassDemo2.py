class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside distructor")

obj1 = Demo()
obj2 = Demo()

print("End of application")