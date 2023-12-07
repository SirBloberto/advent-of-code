file = open("input.txt", "r")
lines = file.readlines()
values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
hands = []
for line in lines:
    line = line.split(" ")
    cards = line[0]
    bet = int(line[1])
    hand = {}
    for card in cards:
        if not hand.get(card):
            hand[card] = 0
        hand[card] += 1
    hand = {k: v for k, v in sorted(hand.items(), key=lambda item: item[1], reverse=True)}
    keys = list(hand.keys())
    value = 0
    extra = 0
    if hand[keys[0]] == 2 and hand[keys[1]] == 2:
        extra = 1
    if hand[keys[0]] == 3:
        if hand[keys[1]] == 2:
            extra = 2
        else:
            extra = 1
    elif hand[keys[0]] > 3:
        extra = 3
    hands.append((hand[keys[0]] + extra, bet, cards))
hands = sorted(hands, key=lambda e: (e[0], values[e[2][0]], values[e[2][1]], values[e[2][2]], values[e[2][3]], values[e[2][4]]))
total = 0
for i, hand in enumerate(hands):
    total += hand[1] * (i + 1)
for hand in hands:
    print(hand[2])
print(total)