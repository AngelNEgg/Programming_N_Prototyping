#Angel Nazaire
#10/21/2024
#Period 5-6

'''Create a guessing game (1-10) that informs the player whether or not their guess was
"Too high" or "Too low", and prints how many attempts it took.
Then, implement a round and difficulty system that functions properly together.

--------------------------------------------------------------------------------------------------'''
import random

rnds = int(input("How many rounds do you want to play: "))
diff = input("What difficulty do you want to play on: ")

if diff == "Easy" or diff == "easy" or diff == "EASY":
	rand = random.randint(1,10)
elif diff == "Medium" or diff == "medium" or diff == "MEDIUM":
    rand = random.randint(1,50)
elif diff == "Hard" or diff == "hard" or diff == "HARD":
    rand = random.randint(1,1000)

tries = 0
guess = "placeholder"

def guess_func(x,y,z,r):
    x = int(input("Guess any number 1-10: "))
    
    if x == y and x == 1:
        z = z + 1
        r = r - 1
        print("\nYou guessed correctly in", str(z), "try!")
        
    elif x == y and x > 1:
        z = z + 1
        r = r - 1
        print("\nYou guessed correctly in", str(z), "tries!")
        
    else:
        if x > y:
            print("Too high...")
            z = z + 1
            r = r - 1
            guess_func(x,y,z,r)
        elif x < y:
            z = z + 1
            r = r - 1
            print("Too low...")
            guess_func(x,y,z,r)
            
guess_func(guess,rand,tries,rounds)
