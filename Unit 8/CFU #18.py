# Angel Nazaire
# 1/7/2024
# Period 5-6
'''Lists Practice'''

prices = []
total = 0

ask = int(input("How many items will you add to your shopping list? "))
for i in range(ask):
    cost = float(input(f"Input the price of item number: {i+1}"))
    print(f"Item 1: {cost}")
    print(prices.append(cost))

for i in range(len(prices)):
    total += prices[i]
    print(f"Item {i}: {prices[i]}")
else:
    print("Your total price is $"+ str(total))
