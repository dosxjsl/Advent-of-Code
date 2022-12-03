file = open("test.txt")
data = file.read().splitlines()
total = 0


def divisible(num1, num2):
    return num1 % num2 == 0


for i in range(len(data)):
    arr = data[i].split()

    for j in range(len(arr)):
        arr[j] = int(arr[j])
    for k in range(len(arr)):
        for l in range(len(arr)):
            if l == k:
                l += 1
            elif divisible(arr[k], arr[l]):
                total += arr[k] / arr[l]
            print(arr[k], arr[l])

print(total)
