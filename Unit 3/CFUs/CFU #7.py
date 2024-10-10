#Angel Nazaire
#10/10/2024
#Period 5-6
'''Create a program that asks the user for three numbers.The main program should send those three numbers as arguments to a function to calculates and prints “The sum of your three numbers is:  XXX”The main program should then send those same numbers to a second function which calculates and prints “The average of your three numbers is:  XXX'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))

tot = (num1 + num2 + num3)

def sum_function(x,y,z):
    
    ans = (x + y + z)
    
    print("The sum of your three numbers is:", str(ans))
    
    return ans

sum_function(num1,num2,num3)

def average_func(ans):
    sol = ans // 3
    print("The average of your three numbers is:", str(sol))
    return sol

average_func(tot)
