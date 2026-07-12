class Arithmatic:
    def Addition(No1,No2):
        Ans = No1 + No2
        return Ans

    def Substraction(No1,No2):
        Ans = No1 - No2
        return Ans

Aobj = Arithmatic()

print("Enter first number :")
Value1 = int(input())

print("Enter second number :")
Value2 = int(input())

Ret = Aobj.Addition(Value1,Value2)   # error
print("Addition is :",Ret)

Ret = Aobj.Substraction(Value1,Value2)   # error
print("Substraction is :",Ret)