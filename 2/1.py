def parse(line):
    game = line.split(":")
    sets = game[1].split(";")
    for set in sets:
        set = set.split(",")
        for pull in set:
            values = pull.split(" ")
            amount = int(values[1])
            type = values[2]
            if type == "green" and amount > 13:
                return 0
            if type == "red" and amount > 12:
                return 0
            if type == "blue" and amount > 14:
                return 0
    return int(game[0].split()[1])

file = open("input.txt", "r")
lines = file.read().splitlines()
total = 0
for line in lines:
    total += parse(line)
print(total)