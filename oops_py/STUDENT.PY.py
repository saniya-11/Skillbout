class student:
    def __init__(self,__name,__marks):
        self.__name = __name
        self.__marks = __marks
    def setName(self,name):
        self.__name = name
    def setMarks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")

    def getName(self):
        return self.__name

    def getMarks(self):
        return self.__marks

s=student("<NAME>","marks")
name=input("Enter your name: ")
marks=int(input("Enter your marks: "))
s.setName(name)
s.setMarks(marks)
print("Name:",s.getName())
print("marks:",s.getMarks())
