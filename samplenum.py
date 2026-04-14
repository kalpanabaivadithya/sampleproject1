
import numpy as np
import random
import math

print("===== ADVANCED PYTHON ALL-IN-ONE PROGRAM =====")


print("\n--- Typecasting & Type Checking ---")
values = ["42", 3.99, True, 100]
for v in values:
    print(f"Value: {v} | Type: {type(v).__name__} | To int: {int(v)}")


print("\n--- Advanced Operators ---")
x, y = 17, 4
print(f"Floor Division: {x} // {y} = {x // y}")
print(f"Modulus:        {x} % {y}  = {x % y}")
print(f"Power:          {x} ** {y} = {x ** y}")
print(f"Bitwise AND:    {x} & {y}  = {x & y}")
print(f"Bitwise OR:     {x} | {y}  = {x | y}")
print(f"Left Shift:     {x} << 1   = {x << 1}")
print(f"Right Shift:    {x} >> 1   = {x >> 1}")

print("\n--- Functions ---")

def power(base, exp=2):
    return base ** exp

def total(*args):
    return sum(args)

def profile(**kwargs):
    for k, v in kwargs.items():
        print(f"  {k}: {v}")

print("Power (default exp=2):", power(5))
print("Power (exp=3):", power(5, 3))
print("Total of 1,2,3,4,5:", total(1, 2, 3, 4, 5))
print("Profile:")
profile(name="Kalpana", age=20, city="Hyderabad")
print("\n--- Control Flow ---")


score = 85
if score >= 90:
    grade = "A+"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
print(f"Score: {score} → Grade: {grade}")


print("First even number > 10:", end=" ")
n = 11
while True:
    if n % 2 == 0:
        print(n)
        break
    n += 1


squares = [i**2 for i in range(1, 6)]
print("Squares (1–5):", squares)
print("\n--- Data Structures --")
nums = [5, 3, 8, 1, 9, 2]
print("Original:", nums)
print("Sorted:", sorted(nums))
print("Reversed:", nums[::-1])
print("Sliced [1:4]:", nums[1:4])


student = {"name": "Kalpana", "marks": [88, 92, 75, 95]}
avg = sum(student["marks"]) / len(student["marks"])
print(f"\nStudent: {student['name']}")
print(f"Marks: {student['marks']}")
print(f"Average: {avg:.2f}")


set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union: {set_a | set_b}")
print(f"Intersection: {set_a & set_b}")
print(f"Difference A-B: {set_a - set_b}")

# ─────────────────────