def delta(list):
    sequence = []
    for i, element in enumerate(list):
        sequence.append(element - list[i - 1])
    sequence.pop(0)
    return sequence

file = open("input.txt", "r")
lines = file.readlines()
readings = [line.strip().split(" ") for line in lines]
total = 0
for i, reading in enumerate(readings):
    difference = [[int(point) for point in reading]]
    while sum(difference[-1]) != 0:
        difference.append(delta(difference[-1]))
    next = [i[-1] for i in reversed(difference)]
    for i in range(1, len(next)):
        next[i] = next[i] + next[i - 1]
    total += next[-1]
print(total)