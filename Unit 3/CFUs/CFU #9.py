# Angel Nazaire
# 10/17/2024
# Period 5-6

import random

rolls = int(input("How many rolls do you want to play? (1-5)"))

num = random.randint(1,6)
score = 0
game = 1

guess = int(input("Guess a number between 1 and 6: "))

if guess == num and rolls >= 1:
    print("Good job!")
    score = score + 6
    game = game + 2
    num = random.randint(1,6)
else:
    print("Too bad...")
    score = score - 1
    game = game + 1
    num = random.randint(1,6)

if guess == num and game == 2 and rolls >= 1:
    print("Good job!")
    score = score + 6
    game = game + 2
    num = random.randint(1,6)
else:
    print("Too bad...")
    score = score - 1
    game = game + 1
    num = random.randint(1,6)
 
if guess == num and game == 3:
    print("Good job!")
    score = score + 6
    game = game + 2
    num = random.randint(1,6)
else:
    print("Too bad...")
    score = score - 1
    game = game + 1
    num = random.randint(1,6)
 
if guess == num and game == 4:
    print("Good job!")
    score = score + 6
    game = game + 2
    num = random.randint(1,6)
else:
    print("Too bad...")
    score = score - 1
    game = game + 1
    num = random.randint(1,6)
 
if guess == num and game == 5:
    print("Good job!")
    score = score + 6
    game = game + 2
else:
    print("Too bad...")
    score = score - 1
    game = game + 1
 
print("Your final score is...\n" + str(score))
# too long
# ----------------------------------------------------------------

