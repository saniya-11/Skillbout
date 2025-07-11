class employee:
    def work(self):
        print("Employee work")
class manager(employee):
    def manage(self):
        print("Manager work")

e = employee()
e.work()

m = manager()
m.work()
m.manage()