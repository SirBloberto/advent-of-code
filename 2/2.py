def parse(line):
    game = line.split(":")
    sets = game[1].split(";")
    r, g, b = 0, 0, 0
    for set in sets:
        set = set.split(",")
        for pull in set:
            values = pull.split(" ")
            amount = int(values[1])
            type = values[2]
            if type == "green" and amount > g:
                g = amount
            if type == "red" and amount > r:
                r = amount
            if type == "blue" and amount > b:
                b = amount
    return r * g * b

file = open("input.txt", "r")
lines = file.read().splitlines()
total = 0
for line in lines:
    total += parse(line)
print(total)