#Designing my Own Class 

# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"


# Child class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)   # initialize parent attributes
        self.os = os
        self.storage = storage
        self.__battery = 100   # private attribute (encapsulation)

    def use(self, hours):
        if self.__battery > 0:
            self.__battery -= hours * 10
            if self.__battery < 0:
                self.__battery = 0
            print(f"Using {self.info()} for {hours}h... Battery now {self.__battery}%")
        else:
            print("Battery empty! Please charge.")

    def charge(self):
        self.__battery = 100
        print(f"{self.info()} is now fully charged 🔋")

    def get_battery(self):
        return self.__battery


# Smartphone objects
phone1 = Smartphone("Samsung", "Galaxy S24", "Android", "256GB")
phone2 = Smartphone("Apple", "iPhone 15", "iOS", "128GB")

print("\n--- Smartphone Demo ---")
phone1.use(3)
phone1.charge()
print(f"{phone2.info()} battery: {phone2.get_battery()}%")


# Polymorphism 

class Vehicle:
    def move(self):
        pass   # placeholder to be overridden


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


print("\n--- Vehicle Polymorphism Demo ---")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
