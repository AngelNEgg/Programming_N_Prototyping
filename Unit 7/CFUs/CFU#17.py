#Angel Nazaire
#1/2/2025
#Period 5-6
'''CFU #17: Review and BuildIn Functions'''

box = "lolipop"
def formating(box):
    userInput = int(input("Choice? (1,2,3,4,5,6)"))
    if userInput == 1:
        #capitalize the first letter of the string
        print(box.capitalize())
        pass
    elif userInput == 2:
        #find and return the position of a value in the string
        print(box.find("i"))
        pass
    elif userInput == 3:
        #return true if the variable is a number
        print(box.isdigit())
        pass
    elif userInput == 4:
        #output the variable all lowercase
        print(box.lower())
        pass
    elif userInput == 5:
        #output the variable all capital
        print(box.upper())
        pass
    elif userInput == 6:
        #replace an index item for another item
        print(box.replace("o", "i"))
        pass
    else:
        print("not a valid option")
        pass
    
formating(box)
