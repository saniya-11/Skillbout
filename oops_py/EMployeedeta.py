class Employee:
    def __init__(self,name,salary,age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def set_name(self,name):
        self.__name = name
    def set_salary(self,salary):
        self.__salary = salary
    def set_age(self,age):
        self.__age = age
    def get_name(self):
        return self.__name
    def get_salary(self):
        if self.__salary > 0:
            return self.__salary
        else:
            return "Salary must be greater than 0"
    def get_age(self):
        if self.__age >=18 :
            return self.__age
        else:
            return "Age must be greater than 18"


name=input("Enter your name: ")
salary=int(input("Enter your salary: "))
age=int(input("Enter your age: "))
employee = Employee(name,salary,age)
employee.set_name(name)
employee.set_salary(salary)
employee.set_age(age)
print("Employee name: ",employee.get_name())
print("Employee salary:",employee.get_salary())
print("Employee age",employee.get_age())