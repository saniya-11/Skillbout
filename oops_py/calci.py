class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return "Error:ZeroDivisionError"

        return a/b

M=int(input("enter first number:"))
S=int(input("enter second number:"))
c=calculator()
print("Addition",c.add(M,S))
print("Subraction",c.sub(M,S))
print("Multiplication",c.mul(M,S))
print("Dividsion",c.div(M,S))