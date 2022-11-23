import math

file = open("Day1.txt")
data = file.read().strip().splitlines()

#--------------FUNCTIONS--------------
def requiredFuel(mass):
    return math.floor(mass/3)-2

#----------------MAIN-----------------
def main():
    total = 0
    for num in data:
        fuel = requiredFuel(int(num))
        while(True):
            total += fuel
            fuel = requiredFuel(fuel)
            if(fuel <= 0):
                break
    print(total)

if __name__ == "__main__":
    main()

