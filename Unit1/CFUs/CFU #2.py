fName = input("What is your first name?")
lName = input("What is your last name?")
age = input("How old are you?")
q1 = input("How many school years have you completed?")
est = int("21") - int(age)

print("Hello, " + fName + " " + lName + "!\n" + "You are " + age + " years old, and have been through " + q1 + " school years so far.")

#The print code below is not part of the main assignment

print("If you are currently " + age + " years old, then you will be 21 in about " + str(est) + " years from now.")
