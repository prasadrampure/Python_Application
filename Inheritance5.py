class Base:
    def Fun(self):
        print("Inside Base constructor")

    

class Derived(Base):
    def sun(self):
        print("Inside Derived sun")

dobj = Derived()

dobj.fun()
dobj.sun()