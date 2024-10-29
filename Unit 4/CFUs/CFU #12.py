#Angel Nazaire
#10/21/2024
#Period 5-6
# --------------------------------------------------------------------------------------------------
#Part 1

'''Create a loop that asks the user for a password,
denies them if it doesn't match "simonsnyc", and ends if it does.'''

passw = "simonsnyc"
userPass = input("What is the password? ")

while userPass != passw:
    print("Wrong Password!")
    userPass = input("What is the password?")
        
print("Correct! You may pass..")
# --------------------------------------------------------------------------------------------------
#Part 2

'''Create a loop that asks the user for a password,
denies them if it doesn't match "simonsnyc", and ends if it does.'''

passw = "simonsnyc"
userPass = input("What is the password? ")
i = 0

# ver1_Func: x = userPass, y = passw
# ver2_Func: x = userPass, y = passw, z = i

def ver1_Func(x,y)
	while userPass != passw:
    	print("Wrong Password!")
    	userPass = input("What is the password?")
        
	print("Correct! You may pass..")
    
def ver2_Func(x,y,z)
for i in range(3):
	while userPass != passw:
    	print("Wrong Password!")
        i += 1
    	userPass = input("What is the password?")
        
	print("Correct! You may pass..")
