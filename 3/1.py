def isvalid(number, i, j):
    start_x = max(j - len(str(number)) - 1, 0)
    end_x = min(j + 1, len(lines))
    start_y = max(i - 1, 0)
    end_y = min(i + 2, len(lines))
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if lines[y][x] != '.' and not lines[y][x].isdigit():
                return number
    return 0

file = open("input.txt", "r")
lines = file.readlines()
total = 0
for i, line in enumerate(lines):
    value = 0
    for j, character in enumerate(line):
        if character.isdigit():
            value = value * 10 + int(character)
        else:
            if value > 0:
                total += isvalid(value, i, j)
            value = 0
print(total)