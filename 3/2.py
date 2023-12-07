def isvalid(number, i, j):
    start_x = max(j - len(str(number)) - 1, 0)
    end_x = min(j + 1, len(lines))
    start_y = max(i - 1, 0)
    end_y = min(i + 2, len(lines))
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if lines[y][x] == '*':
                return number, x, y
    return 0, 0, 0

file = open("input.txt", "r")
lines = file.readlines()
total = 0
gears = {}
for i, line in enumerate(lines):
    value = 0
    for j, character in enumerate(line):
        if character.isdigit():
            value = value * 10 + int(character)
        else:
            if value > 0:
                number, x, y = isvalid(value, i, j)
                key = str(x) + "," + str(y)
                if not gears.get(key):
                    gears[key] = (number, 1)
                else:
                    gears[key] = (gears[key][0] * value, gears[key][1] + 1)
            value = 0
for key in gears:
    if gears[key][1] == 2:
        total += gears[key][0]
print(total)