# Angel Nazaire
# 1/7/2024
# Period 5-6
'''Using the code you learned in class, write a program that calculates 
   the total price of given items.'''

prices = []
items = []
total = 0

ask = int(input("How many items will you add to your shopping list? "))
for i in range(ask):
    names = input(f"What is the name of item number: {i+1}")
    cost = float(input(f"Input the price of item number: {i+1}"))
    items.append(names)
    prices.append(cost)

for i in range(len(items)):
    print(f"{items[i]}: ${prices[i]}")

for i in range(len(prices)):
    total += prices[i]
    
print("Sub Total: $"+ str(total))
