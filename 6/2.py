file = open("input.txt", "r")
lines = file.readlines()
time = int("".join([value for value in lines[0].split(" ")[1:] if value != '' ]))
distance = int("".join([value for value in lines[1].split(" ")[1:] if value != '']))
start, end = 0, 0
for i in range(time):
    if (time - i) * i >= distance:
        start = i
        break
for i in range(time, 0, -1):
    if (time - i) * i >= distance:
        end = i
        break
print(end - start + 1)