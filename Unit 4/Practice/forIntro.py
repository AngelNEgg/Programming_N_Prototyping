# For-Loop Introduction 1

for x in range(5):
    print(x)
# -----------------------------------
# For-Loop Introduction 2

x = 10

for i in range(10,20):
    print(f"Loop #{i-10}, x = {x}")
    x = x + 1
# -----------------------------------
# For-Loop Introduction 3

x = 0

for i in range(5):
    print(x + 1)
for i in range(1,4):
    print(x - 2)
for i in range(2,19,3):
    print(x + 3)
for i in range(0,100,5):
    x = x + 5
    print(x)
