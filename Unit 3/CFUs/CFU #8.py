#Angel Nazaire
#10/15/2024
#Period 5-6
'''Ask the user if they ordered delivery'''

ans1 = input("Did you order food today? ")

if ans1 == "yes" or ans1 == "Yes" or ans1 == "YES":
    ans2 = float(input("How much did it cost? "))
    ans3 = int(input("How many people are you splitting it with? "))
    tot = ans2 / ans3
    print("The cost of the meal per person is about $" + str(tot))
elif ans1 != "yes" or ans1 != "Yes" or ans1 != "YES":
    print("No?? So who is cooking...?")
