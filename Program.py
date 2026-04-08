# program.py - Class, Object, Abstract and Encapsulation

from abc import ABC, abstractmethod

# ─────────────────────────────────────────
# ABSTRACT CLASS
# ─────────────────────────────────────────
class Animal(ABC):

    def __init__(self, name, age):
        # ENCAPSULATION - private variables
        self.__name = name
        self.__age  = age

    # Getter methods (Encapsulation)
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Setter methods (Encapsulation)
    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("Invalid name!")

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!")

    # Abstract methods (must be overridden)
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def describe(self):
        pass

    # Normal method
    def show_info(self):
        print(f"Name : {self.__name}")
        print(f"Age  : {self.__age} years")


# ─────────────────────────────────────────
# CLASS 1 - Dog (inherits Animal)
# ─────────────────────────────────────────
class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed          # private variable

    def get_breed(self):
        return self.__breed

    # Implementing abstract methods
    def sound(self):
        print("Dog says: Woof! Woof!")

    def describe(self):
        print("---- Dog Info ----")
        self.show_info()
        print(f"Breed: {self.__breed}")


# ─────────────────────────────────────────
# CLASS 2 - Cat (inherits Animal)
# ─────────────────────────────────────────
class Cat(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color          # private variable

    def get_color(self):
        return self.__color

    # Implementing abstract methods
    def sound(self):
        print("Cat says: Meow! Meow!")

    def describe(self):
        print("---- Cat Info ----")
        self.show_info()
        print(f"Color: {self.__color}")


# ─────────────────────────────────────────
# CLASS 3 - BankAccount (Encapsulation)
# ─────────────────────────────────────────
class BankAccount:

    def __init__(self, owner, balance):
        self.__owner   = owner        # private
        self.__balance = balance      # private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited  : Rs.{amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdraw amount!")
        else:
            self.__balance -= amount
            print(f"Withdrawn  : Rs.{amount}")

    def show_balance(self):
        print(f"Owner      : {self.__owner}")
        print(f"Balance    : Rs.{self.__balance}")


# ─────────────────────────────────────────
# CLASS 4 - Student (Class & Object)
# ─────────────────────────────────────────
class Student:

    # Class variable
    school_name = "ABC High School"

    def __init__(self, name, marks):
        self.__name  = name           # private
        self.__marks = marks          # private

    def get_name(self):
        return self.__name

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks must be between 0 and 100!")

    def grade(self):
        if self.__marks >= 90:
            return "A+"
        elif self.__marks >= 80:
            return "A"
        elif self.__marks >= 70:
            return "B"
        elif self.__marks >= 60:
            return "C"
        else:
            return "F"

    def show_info(self):
        print(f"School     : {Student.school_name}")
        print(f"Name       : {self.__name}")
        print(f"Marks      : {self.__marks}")
        print(f"Grade      : {self.grade()}")


# ─────────────────────────────────────────
# MAIN PROGRAM - Creating Objects
# ─────────────────────────────────────────

print("=" * 40)
print("       ANIMAL - DOG & CAT           ")
print("=" * 40)

# Dog Object
dog = Dog("Bruno", 3, "Labrador")
dog.describe()
dog.sound()

print()

# Cat Object
cat = Cat("Kitty", 2, "White")
cat.describe()
cat.sound()

# Using Setter (Encapsulation)
print("\n-- Updating Dog Name --")
dog.set_name("Max")
print("Updated Name:", dog.get_name())

print("\n" + "=" * 40)
print("       BANK ACCOUNT                 ")
print("=" * 40)

# BankAccount Object
account = BankAccount("Ravi", 5000)
account.show_balance()
print()
account.deposit(2000)
account.withdraw(1000)
account.withdraw(9000)   # Insufficient
print()
account.show_balance()

print("\n" + "=" * 40)
print("         STUDENTS                   ")
print("=" * 40)

# Student Objects
s1 = Student("Asha",  95)
s2 = Student("Ravi",  78)
s3 = Student("Priya", 55)

for student in [s1, s2, s3]:
    student.show_info()
    print()

# Using Setter
print("-- Updating Ravi's Marks --")
s2.set_marks(85)
print("Updated Marks:", s2.get_marks())
print("Updated Grade:", s2.grade())