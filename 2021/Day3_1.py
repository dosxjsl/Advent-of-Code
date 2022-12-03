import re
import math
import random

file = open("Day3.txt").read().strip().splitlines()

# ______________________FUNCTIONS______________________
def binaryToDecimal(binary):

    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def invertBits(num):

    # # calculating number of bits in the number
    # x = int(math.log2(num)) + 1

    # # Inverting the bits one by one
    # for i in range(x):
    #     num = num ^ (1 << i)
    num = list(num)
    for i, digit in enumerate(num):
        if digit == "0":
            num[i] = "1"
        else:
            num[i] = "0"
    num = "".join(num)

    return num


def getMostCommonDigits(input):
    arr = ""

    for i in range(len(input[0])):
        zeroes = 0
        ones = 0
        for line in input:
            if line[i] == "0":
                zeroes += 1
            elif line[i] == "1":
                ones += 1

        if zeroes > ones:
            arr += "0"
        else:
            arr += "1"

    return arr


# ______________________MAIN______________________
def main():
    binaryNum = getMostCommonDigits(file)
    gamma_rate = binaryToDecimal(int(binaryNum))
    epsilon_rate = binaryToDecimal(int(invertBits(binaryNum)))

    power_rate = gamma_rate * epsilon_rate
    print(power_rate)


if __name__ == "__main__":
    main()
