import numpy as np


temps = np.array([32, 35, 30, 31, 36, 34, 33])


def average_temp(data):
    return np.mean(data)

def max_temp(data):
    return np.max(data)

def min_temp(data):
    return np.min(data)

def hot_days(data):
    return np.where(data > 33, "Hot", "Normal")

def temperature_difference(data):
    return np.max(data) - np.min(data)



print(" Weekly Temperature Data:", temps)

avg = average_temp(temps)
print("\n Average Temperature:", avg)

print("\n Highest Temperature:", max_temp(temps))
print(" Lowest Temperature:", min_temp(temps))

status = hot_days(temps)
print("\n Day Status (Hot/Normal):", status)

diff = temperature_difference(temps)
print("\n Temperature Difference:", diff)