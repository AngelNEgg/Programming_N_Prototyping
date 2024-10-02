#remove total change from bills

a = int(input("How many pennies do you have?"))
b = int(input("How many nickles do you have?"))
c = int(input("How many dimes do you have?"))
d = int(input("How many quarters do you have?"))
e = int(input("How many loonies '($1)' do you have?"))
f = int(input("How many toonies '($2)' do you have?"))

tot = (a + (b*5) + (c*10) + (d*25) + (e*100) + (f*200))/100

totDol = int(tot // 1)
        
print("The number of pennies is " + str(a))
print("The number of nickles is " + str(b))
print("The number of dimes is " + str(c))
print("The number of quarters is " + str(d))
print("The number of loonies is " + str(e))
print("The number of toonies is " + str(f))

print("\nThe total amount of money in dollars is $" + str(tot))

change = tot - totDol # stores the value of the cents from the total amout of money
changeQ = (change) % 4

chq = int(change * 4)
chd = int(change * 10) - chq
chn = int(change * 20) - (chd * 2)
chp = int(change * 100) - (chn * 5) - (chd * 10)

dollars = int((tot - totDol))

print("You have $" + str(totDol) + ",", str(chq), "quarters,",str(chn),"nickles,",str(chd),"dimes, and",str(chp),"penny(ies) in change alone.")
