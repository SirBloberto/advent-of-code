file = open("input.txt", "r")
lines = file.read().splitlines()
total = 0
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def forward(line):
    for i in range(0, len(line)):
        if line[i].isdigit():
            return int(line[i]) * 10
        for j, number in enumerate(numbers):
            if line.startswith(number, i):
                return (j + 1) * 10


def reverse(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return int(line[i])
        for j, number in enumerate(numbers):
            if line.endswith(number, 0, i + 1):
                return (j + 1)


for line in lines:
    total += forward(line)
    total += reverse(line)
print(total)