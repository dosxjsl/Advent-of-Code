import math

file = open("Day1.txt")
data = file.read().strip().splitlines()

def requiredFuel(mass):
    return math.floor(mass/3)-2

# print(requiredFuel(100756))
total = 0

for num in data:
    fuel = requiredFuel(int(num))
    total += fuel

print(total)