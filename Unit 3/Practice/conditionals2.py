#IF and ELSE
num = int(input("Enter a number: "))

if num >= 5:
    print(str(num),"is greater than or equal to 5!")
    
else:
    print(str(num),"is less than or equal to 5!")
-------------------------------------------------------------
#IF, ELSE, and ELSE IF
num = int(input("Enter a number: "))

if num >= 1:
    print(str(num),"is a positive number!")
    
elif num < 0:
    print(str(num), "is a negative number...")
    
else:
    print(str(num),"can't be positive or negative.")
