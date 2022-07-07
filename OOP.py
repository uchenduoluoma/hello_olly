class car:
    count_car = 0
    count_car += 1
    print (count_car)

    def __init__ (self, model="Benz", color="blue"):
        self.model = model
        self.color = color
        self.fuel = 10

    def set_color (self, color):
        set_color = color

    def move (self, distance, D = "forward", angle = 0):
        if (self.fuel < distance * 0.5):
            print ("insuficient fuel")
            x = 2 * self.fuel
            print(f"you can only go {x} meters")
        else:
            print(f"your car moved {distance} meters {D} at angle {angle}")
            self.fuel = distance * 0.5
            print(f"you have {self.fuel}L of fuel remaining")


car3 = car()
car1 = car("Toyota")
car2 = car("Toyota", "red")

print(car1.fuel)
car1.move(4)
print (car1.fuel)
car1.move (1000)

def refill(amount):
    self.fuel += amount

def get_fuel():
    return self.fuel