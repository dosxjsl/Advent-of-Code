# Advent of Code: Day 12
import re
import json

f = open("D12.txt")
string = f.read()
f.close()


# Part 2
def hook(obj):
    if "red" in obj.values():
        return {}
    else:
        return obj


stuff = str(json.loads(string, object_hook=hook))
print(sum(map(int, re.findall("-?[0-9]+", stuff))))
