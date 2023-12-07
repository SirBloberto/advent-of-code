def translate(i):
    while i < len(lines) and lines[i] != "\n":
        line = lines[i].strip().split(" ")
        line = list(map(int, line))
        for j, seed in enumerate(seeds):
            if seed[0] >= line[1] and seed[0] < line[1] + line[2] and not seeds[j][1]:
                seeds[j] = (seed[0] - line[1] + line[0], True)
        i += 1
    return i


file = open("input.txt", "r")
lines = file.readlines()
data = []
seeds = lines[0].strip().split(": ")[1].split(" ")
for i, seed in enumerate(seeds):
    seeds[i] = (int(seeds[i]), False)
i = 3
while i < len(lines):
    i = translate(i)
    for j, seed in enumerate(seeds):
        seeds[j] = (seeds[j][0], False)
    i += 2
print(sorted(seeds)[0][0])