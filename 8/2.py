import math

file = open("input.txt", "r")
lines = file.readlines()
instructions = lines[0][:-1]
map = {}
for line in lines[2:]:
    data = line.strip().split(" = ")
    tuple = data[1][1:-1].split(", ")
    map[data[0]] = (tuple[0], tuple[1])
total = 0
current = [i for i in map.keys() if i.endswith('A')]
total = []
for i, value in enumerate(current):
    time = 0
    while True:
        direction = instructions[time % len(instructions)]
        if direction == "L":
            current[i] = map[current[i]][0]
        if direction == "R":
            current[i] = map[current[i]][1]
        time += 1
        if current[i].endswith('Z'):
            total.append(time)
            break
print(math.lcm(*total))