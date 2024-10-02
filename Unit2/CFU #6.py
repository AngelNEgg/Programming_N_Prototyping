import math
import random

num = int(input("Enter any number: "))
rand = int(random.randrange(1,100))

print("Random number generated: ", str(rand))
print("The number input: ", str(num))

summ = num + rand
diff = rand - num
prod = num * rand
quot = num / rand
rema = num % rand
sqrt = math.sqrt(rand)
expo = math.pow(num,rand)

print("The results for the random and input numbers are shown here;\n")

print("Addition:\n",str(num),"+",str(rand),"=",str(summ)+"\n")
print("Subtraction:\n",str(num),"-",str(rand),"=",str(diff)+"\n")
print("Multiplicaion:\n",str(num),"*",str(rand),"=",str(prod)+"\n")
print("Division:\n",str(num),"/",str(rand),"=",str(quot)+"\n")
print("Remainder:\n",str(num),"%",str(rand),"=",str(rema)+"\n")
print("Square Root:\n","√" + str(rand),"=",str(sqrt)+"\n")
print("Exponent:\n",str(num),"^",str(rand),"=",str(expo)+"\n")
