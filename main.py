import random

heads, tails, throws, flip, streak = 0, 0, 0, 0, 0
sequence = []
longestStreak = 1
lastFlip = ""
desiredThrows = int(input("Desired throws?: "))

for throws in range(desiredThrows):
    flip = random.randint(0, 1)
    if flip == 0:
        heads += 1
        sequence.append("Heads, ")
        if lastFlip == "Heads":
            streak += 1
        else:
            streak = 1
        if streak > longestStreak:
            longestStreak = streak
        lastFlip = "Heads"

    else:
        tails += 1
        sequence.append("Tails, ")
        if lastFlip == "Tails":
            streak += 1
        else:
            streak = 1
        if streak > longestStreak:
            longestStreak = streak
        lastFlip = "Tails"
    throws += 1

print("Heads: ", heads)
print("Tails: ", tails)
print("Longest Streak: ", longestStreak)
if input("Print Sequence? (y/n):") == "y" or "Y":
    print("Sequence: ", sequence)
