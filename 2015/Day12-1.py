import re

file = open("D12.txt")
# str = file.read()
total = 0

for line in file:
    nums = re.findall("[-+]?\d+", line)
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    for i in nums:
        total += i

print(total)
# print("Sum of all numbers 1:", sum(map(int, re.findall("-?[0-9]+", string))))
# file.close()
