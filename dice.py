import random
roll = "Y"
count = 1

while roll == "Y":
    question = input("Do you want to roll the dice? [Y/N]")
    roll = question
    if roll == "Y":
        roll1 = True
    else:
        roll1 = False

    if roll1:
        dice = random.randint(0,6)
        print("Dice {}: {}".format(count, str(dice)))
    count = count + 1


print("Game over")