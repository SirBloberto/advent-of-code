file = open("test.txt", "r")
lines = file.read().splitlines()
total = 0
for line in lines:
    for i in range(0, len(line)):
        if line[i].isdigit():
            total += int(line[i]) * 10
            break
    for i in range(len(line) - 1, 0, -1):
        if line[i].isdigit():
            total += int(line[i])
            break
print(total)
