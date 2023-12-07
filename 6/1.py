import math

file = open("input.txt", "r")
lines = file.readlines()
times = [int(value) for value in lines[0].split(" ")[1:] if value != '' ]
distances = [int(value) for value in lines[1].split(" ")[1:] if value != '']
values = [0] * len(times)
for i in range(len(values)):
    for j in range(times[i]):
        if (times[i] - j) * j >= distances[i]:
            print(times[i], distances[i], j)
            values[i] += 1
print(math.prod(values))