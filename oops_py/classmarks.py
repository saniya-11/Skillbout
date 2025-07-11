class Marks:
    def __init__(self):
        self.__math_marks = 0

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__math_marks = marks
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")

    def get_marks(self):
        print("Math Marks:", self.__math_marks)

m = Marks()
marks_input = int(input("Enter Math Marks: "))
m.set_marks(marks_input)
m.get_marks()
