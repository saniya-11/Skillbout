from abc import ABC, abstractmethod
class paymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPI(paymentMethod):
    def pay(self,amount):
        print(f"paid: {amount} Via UPI")

upi=UPI()
upi.pay(100)
