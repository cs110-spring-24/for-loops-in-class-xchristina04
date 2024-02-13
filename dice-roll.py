import random
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for rolls in range(100):
    dice = random.randint(1, 6)
    if (dice == 1):
        one += 1
    elif (dice == 2):
        two += 1
    elif (dice == 3):
        three += 1
    elif (dice == 4):
        four += 1
    elif (dice == 5):
        five += 1
    else:
        six += 1
    print(dice)
print(f"After 100 rolls, we rolled {one} 1s, {two} 2s, {three} 3s, {four} 4s, {five} 5s, and {six} 6s.")