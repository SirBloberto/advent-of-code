file = open("input.txt", "r")
lines = file.readlines()
total = 0
for line in lines:
    parts = line.split(" | ")
    winning = parts[0].split(": ")[1].split(" ")
    for j in range(len(winning)):
        if winning[j] == '':
            continue
        winning[j] = int(winning[j])
    numbers = parts[1].strip().split(" ")
    value = 0
    for number in numbers:
        if number == '':
            continue
        if int(number) in winning:
            if value == 0:
                value = 1
            else:
                value *= 2
    total += value
print(total)