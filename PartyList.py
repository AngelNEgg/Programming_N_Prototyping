people = ["Fahim A", "Arafath A", "Grace C", "William C", "Nibrus C", "Edwin D", "Amelia D", "Sheldon G", "Aarya H", "Sarika I", "Farhan K", "Malachi K", "Syeda M", "Emirah M", "Cesar M", "Nafisa N", "Neelam P", "Marisa R", "Romina R"]

donation = ["Pizza", "Fries", "Cake", "Chips", "Drinks", "Pizza", "Fries", "Cake", "Chips", "Drinks", "Pizza", "Fries", "Cake", "Chips", "Drinks", "Pizza", "Fries", "Cake", "Chips"]


for item in people:
    print("This is my friend,", item + "!")
    
print("\n")
for item in range(19):
    print(f"{people[item]} will bring {donation[item]}!")
