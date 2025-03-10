# Angel Nazaire
# 3/10/25
# Period 5-6
'''Python Code Challenge #6: Make a function to see if the side lengths add up to be a triangle'''

def is_triangle(x,y,z):
    if (x+y) < z:
        print("No")     
    else:
        print("Yes")
        
def input_num():
    num1 = int(input("What is the first side length?"))
    num2 = int(input("What is the second side length?"))
    num3 = int(input("What is the third side length?"))
    
    is_triangle(num1,num2,num3)
    
input_num()
