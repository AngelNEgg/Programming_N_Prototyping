#remove total change from bills

a = int(input("How many pennies do you have?"))
b = int(input("How many nickles do you have?"))
c = int(input("How many dimes do you have?"))
d = int(input("How many quarters do you have?"))
e = int(input("How many loonies '($1)' do you have?"))
f = int(input("How many toonies '($2)' do you have?"))

tot = (a + (b*5) + (c*10) + (d*25) + (e*100) + (f*200))/100

totDol = int((tot // 1))
        
print("The number of pennies is " + str(a))
print("The number of nickles is " + str(b))
print("The number of dimes is " + str(c))
print("The number of quarters is " + str(d))
print("The number of loonies is " + str(e))
print("The number of toonies is " + str(f))

print("\nThe total amount of money in dollars is $" + str(tot))

change = tot - (tot // 1) # stores the value of the cents from the total amout of money

chq = int(change // 0.25)
chd = int((change - (change * 0.25)) // 0.10)
chn = int((change - (change * 0.25) - (change * 0.10)) // 0.05)
chp = int((change - (change * 0.25) - (change * 0.10) - (change * 0.05)) // 0.01)

dollars = int((tot - totDol))

print("You have $" + str(totDol) + ",", str(chq), "quarters,",str(chn),"nickles,",str(chd),"dimes, and",str(chp),"pennies in change alone.")
