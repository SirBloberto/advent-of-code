file = open("input.txt", "r")
lines = file.readlines()
cards = {}
for i in range(len(lines)):
    cards[i] = 1
for i, line in enumerate(lines):
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
            value += 1
    for j in range(value):
        cards[i + j + 1] += cards[i]
total = 0
for i in cards:
    total += cards[i]
print(cards, total)