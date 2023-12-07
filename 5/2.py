def translate(i):
    while i < len(lines) and lines[i] != "\n":
        line = lines[i].strip().split(" ")
        line = list(map(int, line))
        source, start, end = line[0], line[1], line[1] + line[2] -1
        for j, seed in enumerate(seeds):
            seed_start, seed_end = seed[0], seed[1]
            if seed[2]:
                continue
            if start <= seed_start and end >= seed_end:
                seeds[j] = (seed_start - start + source, seed_end - start + source, True)
            elif start > seed_start and start <= seed_end and end > seed_end:
                seeds[j] = (source, seed_end - start + source, True)
                seeds.append((seed_start, start - 1, False))
            elif end < seed_end and end >= seed_start and start < seed_start:
                seeds[j] = (seed_start - start + source, end - seed_start + seed_start - start + source, True)
                seeds.append((end + 1, seed_end, False))
            elif start > seed_start and end < seed_end:
                seeds[j]  = (source, end - seed_start + seed_start - start + source, True)
                seeds.append((seed_start, start - 1, False))
                seeds.append((end + 1, seed_end, False))
        i += 1
    return i


file = open("input.txt", "r")
lines = file.readlines()
data = []
values = lines[0].strip().split(": ")[1].split(" ")
seeds = []
for i in range(0, len(values), 2):
    seeds.append((int(values[i]), int(values[i]) + int(values[i + 1]) - 1, False))
total = 0
i = 3
while i < len(lines):
    i = translate(i)
    for j, seed in enumerate(seeds):
        seeds[j] = (seeds[j][0], seeds[j][1], False)
    i += 2
print(sorted(seeds)[0])