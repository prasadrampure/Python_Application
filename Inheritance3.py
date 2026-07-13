class Base:
    def __init__(self):
        print("Inside Base constructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside Derived constructor")

dobj = Derived()