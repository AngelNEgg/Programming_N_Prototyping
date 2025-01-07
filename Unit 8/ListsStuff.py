# Angel Nazaire
# 1/7/2024
# Period 5-6
'''Lists Practice'''

# Built-In List Commands
## Len(): Function | Counts how many items are in a list
## .Append(): Method | Adds an item to the specified list
## .Insert(): Method | Adds an item in the specified list according to the number placement given
## .Remove(): Method | Removes the specified item from the given list

names = ["Aarya", "Amelia", "Arafath", "Cesar", "Edwin", "Emirah", "Evelyn", "Fahim", "Farhan", "Hailey", "Harbans", "Malachi", "Marisa", "Mia", "Nafisa", "Neelam", "Nibrus", "Romina", "Sarika", "Sharena", "Syeda", "William"]
ages = [14,15,16,17,18,19,20,21,22,23,24,25]
test = 0
for i in range(len(names)):
    i += 1
    print(i)

for i in range(len(ages)):
    print("Oh")
    
groceries = ["Eggs", "Bacon", "Milk", "Flour"]
prices = [1.95, 4.5, 0.99, 5.99]

for item in groceries:
    print('I really like to cook with', item)

total = 0.00

for item in prices:
    total += item
    print(total)
    
print(groceries.append("Apples"))
for item in groceries:
    print('I really like to cook with', item)

print(groceries.insert(5,"lol"))
for item in groceries:
    print('I really like to cook with', item)

print(groceries.remove("Apples"))
for item in groceries:
    print('I really like to cook with', item)
