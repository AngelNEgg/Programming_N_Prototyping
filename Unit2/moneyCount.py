#Code Complete

a = int(input("How many pennies do you have?"))
b = int(input("How many nickles do you have?"))
c = int(input("How many dimes do you have?"))
d = int(input("How many quarters do you have?"))
e = int(input("How many loonies do you have?"))
f = int(input("How many toonies do you have?"))

tot = (a + (b*5) + (c*10) + (d*25) + (e*100) + (f*200))/100

totDol = int(tot // 1)
        
print("The number of pennies is " + str(a))
print("The number of nickles is " + str(b))
print("The number of dimes is " + str(c))
print("The number of quarters is " + str(d))
print("The number of loonies is " + str(e))
print("The number of toonies is " + str(f))

print("\nThe total amount of money in dollars is " + str(tot))

print("\nAnother way to write this is $" + str(totDol) + ", " + str(f) + " toonies, " + str(e) + " loonies, " + str(d) + " quarters, " + str(c) + " dimes, " + str(b) + " nickles, and " + str(a) + " pennies.")
