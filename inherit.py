# program.py - Polymorphism and Inheritance

# ─────────────────────────────────────────
# BASE CLASS 1 - Shape (Inheritance)
# ─────────────────────────────────────────
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0

    def perimeter(self):
        return 0

    def show_info(self):
        print(f"Color     : {self.color}")
        print(f"Area      : {self.area()}")
        print(f"Perimeter : {self.perimeter()}")


# ─────────────────────────────────────────
# CHILD CLASS 1 - Circle
# ─────────────────────────────────────────
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    # Polymorphism - overriding area()
    def area(self):
        return round(3.14 * self.radius * self.radius, 2)

    # Polymorphism - overriding perimeter()
    def perimeter(self):
        return round(2 * 3.14 * self.radius, 2)

    def describe(self):
        print("---- Circle ----")
        self.show_info()
        print(f"Radius    : {self.radius}")


# ─────────────────────────────────────────
# CHILD CLASS 2 - Rectangle
# ─────────────────────────────────────────
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width  = width

    # Polymorphism - overriding area()
    def area(self):
        return self.length * self.width

    # Polymorphism - overriding perimeter()
    def perimeter(self):
        return 2 * (self.length + self.width)

    def describe(self):
        print("---- Rectangle ----")
        self.show_info()
        print(f"Length    : {self.length}")
        print(f"Width     : {self.width}")


# ─────────────────────────────────────────
# CHILD CLASS 3 - Triangle
# ─────────────────────────────────────────
class Triangle(Shape):
    def __init__(self, color, a, b, c, base, height):
        super().__init__(color)
        self.a      = a
        self.b      = b
        self.c      = c
        self.base   = base
        self.height = height

    # Polymorphism - overriding area()
    def area(self):
        return round(0.5 * self.base * self.height, 2)

    # Polymorphism - overriding perimeter()
    def perimeter(self):
        return self.a + self.b + self.c

    def describe(self):
        print("---- Triangle ----")
        self.show_info()
        print(f"Sides     : {self.a}, {self.b}, {self.c}")


# ─────────────────────────────────────────
# BASE CLASS 2 - Employee (Inheritance)
# ─────────────────────────────────────────
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name   = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_bonus(self):
        return 0

    def show_info(self):
        print(f"Name      : {self.name}")
        print(f"EMP ID    : {self.emp_id}")
        print(f"Salary    : Rs.{self.salary}")
        print(f"Bonus     : Rs.{self.calculate_bonus()}")
        print(f"Total Pay : Rs.{self.salary + self.calculate_bonus()}")


# ─────────────────────────────────────────
# CHILD CLASS 4 - Manager
# ─────────────────────────────────────────
class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    # Polymorphism - overriding calculate_bonus()
    def calculate_bonus(self):
        return self.salary * 0.30   # 30% bonus

    def describe(self):
        print("---- Manager ----")
        self.show_info()
        print(f"Department: {self.department}")


# ─────────────────────────────────────────
# CHILD CLASS 5 - Developer
# ─────────────────────────────────────────
class Developer(Employee):
    def __init__(self, name, emp_id, salary, language):
        super().__init__(name, emp_id, salary)
        self.language = language

    # Polymorphism - overriding calculate_bonus()
    def calculate_bonus(self):
        return self.salary * 0.20   # 20% bonus

    def describe(self):
        print("---- Developer ----")
        self.show_info()
        print(f"Language  : {self.language}")


# ─────────────────────────────────────────
# CHILD CLASS 6 - Intern
# ─────────────────────────────────────────
class Intern(Employee):
    def __init__(self, name, emp_id, salary, duration):
        super().__init__(name, emp_id, salary)
        self.duration = duration

    # Polymorphism - overriding calculate_bonus()
    def calculate_bonus(self):
        return self.salary * 0.05   # 5% bonus

    def describe(self):
        print("---- Intern ----")
        self.show_info()
        print(f"Duration  : {self.duration} months")


# ─────────────────────────────────────────
# BASE CLASS 3 - Vehicle (Multilevel)
# ─────────────────────────────────────────
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def fuel_type(self):
        return "Unknown"

    def show_info(self):
        print(f"Brand     : {self.brand}")
        print(f"Speed     : {self.speed} km/h")
        print(f"Fuel Type : {self.fuel_type()}")


# ─────────────────────────────────────────
# CHILD CLASS 7 - Car
# ─────────────────────────────────────────
class Car(Vehicle):
    def __init__(self, brand, speed, model):
        super().__init__(brand, speed)
        self.model = model

    # Polymorphism - overriding fuel_type()
    def fuel_type(self):
        return "Petrol"

    def describe(self):
        print("---- Car ----")
        self.show_info()
        print(f"Model     : {self.model}")


# ─────────────────────────────────────────
# CHILD CLASS 8 - Truck (Multilevel)
# ─────────────────────────────────────────
class Truck(Vehicle):
    def __init__(self, brand, speed, capacity):
        super().__init__(brand, speed)
        self.capacity = capacity

    # Polymorphism - overriding fuel_type()
    def fuel_type(self):
        return "Diesel"

    def describe(self):
        print("---- Truck ----")
        self.show_info()
        print(f"Capacity  : {self.capacity} tons")


# ─────────────────────────────────────────
# CHILD CLASS 9 - ElectricCar (Multilevel)
# ─────────────────────────────────────────
class ElectricCar(Car):
    def __init__(self, brand, speed, model, battery):
        super().__init__(brand, speed, model)
        self.battery = battery

    # Polymorphism - overriding fuel_type()
    def fuel_type(self):
        return "Electric"

    def describe(self):
        print("---- Electric Car ----")
        self.show_info()
        print(f"Model     : {self.model}")
        print(f"Battery   : {self.battery} kWh")


# ─────────────────────────────────────────
# MAIN PROGRAM
# ─────────────────────────────────────────

print("=" * 40)
print("       SHAPES - POLYMORPHISM        ")
print("=" * 40)

# Creating Objects
c = Circle("Red", 7)
r = Rectangle("Blue", 10, 5)
t = Triangle("Green", 3, 4, 5, 4, 3)

# Polymorphism - same method, different results
shapes = [c, r, t]
for shape in shapes:
    shape.describe()
    print()

print("=" * 40)
print("      EMPLOYEES - INHERITANCE       ")
print("=" * 40)

# Creating Objects
m = Manager("Ravi",   "E001", 50000, "IT")
d = Developer("Asha", "E002", 40000, "Python")
i = Intern("Kiran",   "E003", 15000, 6)

# Polymorphism - same method, different bonus
employees = [m, d, i]
for emp in employees:
    emp.describe()
    print()

print("=" * 40)
print("    VEHICLES - MULTILEVEL           ")
print("=" * 40)

# Creating Objects
car = Car("Toyota",       120, "Camry")
truck = Truck("Volvo",     80, 20)
ecar  = ElectricCar("Tesla", 200, "Model 3", 100)

# Polymorphism - same method, different fuel
vehicles = [car, truck, ecar]
for vehicle in vehicles:
    vehicle.describe()
    print()