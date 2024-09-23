'''
	This program calculates the perimeter of a 
  rectangle using input from the user.
'''


#Getting the length from the user
length = int(input("What is the length of the rectangle?"))
width = int(input("What is the width of the rectangle?"))

perimeter = 2 * (length + width)

print("the perimeter is " + str(perimeter))
