from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand, fuel_capacity):
        self._brand = brand                          # Encapsulation
        self._fuel = 0
        self._km_run = 0
        self._fuel_capacity = fuel_capacity

    @abstractmethod
    def start(self): pass

    @abstractmethod
    def stop(self): pass

    def refuel(self, liters):
        if self._fuel + liters > self._fuel_capacity:
            print(f"{self._brand}: Cannot refuel beyond fuel capacity.")
        else:
            self._fuel += liters
            print(f"{self._brand}: Refueled {liters}L. Current fuel: {self._fuel}L")

    def trip(self, distance, mileage):
        fuel_required = distance / mileage
        if self._fuel >= fuel_required:
            self._fuel -= fuel_required
            self._km_run += distance
            print(f"{self._brand}: Trip of {distance} km completed.")
        else:
            print(f"{self._brand}: Not enough fuel for the trip.")

    def needs_service(self):
        return self._km_run >= 10000

    def summary(self):
        print(f"{self.__class__.__name__} - Brand: {self._brand}, Fuel: {self._fuel}L, KM Run: {self._km_run}")
        print(f"{self._brand} is a {self.__class__.__name__}")
        print("Needs Service" if self.needs_service() else " Does Not Need Service")


# Subclasses implementing abstraction and polymorphism
class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, fuel_capacity=50)

    def start(self):
        print(f"{self._brand} Car is starting...")

    def stop(self):
        print(f"{self._brand} Car is stopping...")


class Bike(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, fuel_capacity=15)

    def start(self):
        print(f"{self._brand} Bike is starting...")

    def stop(self):
        print(f"{self._brand} Bike is stopping...")


class Truck(Vehicle):
    def __init__(self, brand):
        super().__init__(brand, fuel_capacity=300)

    def start(self):
        print(f"{self._brand} Truck is starting...")

    def stop(self):
        print(f"{self._brand} Truck is stopping...")

def main():
    print("=== Vehicle Actions ===")
    toyota = Car("Toyota")
    toyota.start()
    toyota.refuel(30)
    toyota.trip(200, mileage=15)  # 13.33L
    toyota.stop()
    print()

    yamaha = Bike("Yamaha")
    yamaha.start()
    yamaha.refuel(30)
    yamaha.stop()
    print()

    volvo = Truck("Volvo")
    volvo.start()
    volvo.refuel(30)
    volvo.trip(200, mileage=5)  # needs 40L, overdrawn fuel for demonstration
    volvo.stop()
    print()

    # Manually set distance for testing service condition
    toyota._km_run = 10200

    print("=== Fleet Summary ===")
    for vehicle in [toyota, yamaha, volvo]:
        vehicle.summary()
        print()

if __name__ == "__main__":
    main()
