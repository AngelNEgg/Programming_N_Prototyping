# area for irregular room

a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))
d = int(input("Enter side D: "))
e = int(input("Enter side E: "))

length = a
width = d
height = a - c

mainArea = length * b

squLength = d - (b + e)

triArea = 0.5*e*height

squArea = squLength * height

roomArea = mainArea + squArea + triArea

print("\nRoom Area:", str(roomArea))
