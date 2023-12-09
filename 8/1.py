file = open("input.txt", "r")
lines = file.readlines()

instructions = lines[0][:-1]

map = {}
for line in lines[2:]:
    data = line.strip().split(" = ")
    tuple = data[1][1:-1].split(", ")
    map[data[0]] = (tuple[0], tuple[1])
total = 0
current = 'AAA'
while True:
    direction = instructions[total % len(instructions)]
    if direction == "L":
        current = map[current][0]
    if direction == "R":
        current = map[current][1]
    total += 1
    if current == 'ZZZ':
        break
print(total)