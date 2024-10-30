
#Angel Nazaire
#10/29/2024
#Period 5-6
# --------------------------------------------------------------------------------------------------

'''Create a loop that asks the user for a password,
denies them if it doesn't match "simonsnyc", and ends if it does*.
(*In version 2, this action will be counted up to three times. Afterwards, the loop will end.)'''

userPass = "placeholder"
version = int(input("Which version do you want to use?(1 or 2)"))

def userInput(x):
    x = input("What is the password?")
    return x

passw = "simonsnyc"
i = 0

def ver1_Func(x,y):
    userInput(userPass)
    while x != y:
        print("Wrong Password!")
        userInput(userPass)
        
    print("Correct! You may pass..")
    
def ver2_Func(x,y,z):
    userInput(userPass)
    for z in range(3):
        while x != y:
            print("Wrong Password!")
            z += 1
            userInput(userPass)
        
        print("Correct! You may pass..")

if version == 1:
    print("Starting version 1...\n")
    ver1_Func(userPass,passw)
elif version == 2:
    print("Starting version 2...\n")
    ver2_Func(userPass,passw,i)
 
