#Angel Nazaire
#10/21/2024
#Period 5-6

'''Create a guessing game (1-10) that informs the player whether or not their guess was
"Too high" or "Too low", and prints how many attempts it took.

--------------------------------------------------------------------------------------------------'''
import random

rand = random.randint(1,10)
tries = 0
guess = "placeholder"

def guess_func(x,y,z):
    x = int(input("Guess any number 1-10: "))
    
    if x == y:
        z = z + 1
        print("\nYou guessed correctly in", str(z), "tries!")
        
    else:
        if x > y:
            print("Too high...")
            z = z + 1
            guess_func(x,y,z)
        elif x < y:
            z = z + 1
            print("Too low...")
            guess_func(x,y,z)

guess_func(guess,rand,tries)
