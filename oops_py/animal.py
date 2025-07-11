class animals:
    def sound(self):
        print("Animals sound")
class cat(animals):
    def sound(self):
        print("Cat Sounding... meow meow")
class dog(animals):
    def sound(self):
        print("Dog Sounding... bow bow")
a=animals()
for a in [cat(), dog()]:
    a.sound()