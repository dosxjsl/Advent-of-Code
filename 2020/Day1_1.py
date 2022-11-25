import math

file = open("Day1.txt").read().strip().splitlines()
file = [int(i) for i in file]
#--------------FUNCTIONS--------------

#----------------MAIN-----------------
def main():
    for i in range(len(file)):
        for j in range(len(file)):
            if (i != j) & (file[i] + file[j] == 2020):
                print(file[i],file[j],file[i] * file[j])

if __name__ == "__main__":
    main()

