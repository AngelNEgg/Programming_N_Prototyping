# Q1
import math

def q1():
    print("Question 1 Answer (Volume of a Sphere):")
    def volume(r): # 'r' will be the radius
        x = (4/3)*math.pi*(r**3)
        return x
    
    r = volume(5) # sets the radius to 5 and completes the equation
    print(f"The volume of the sphere is {r:.2f}.\n") # prints the volume with only the first two decimals
    
# Q2
def q2():
    print("Question 2 Answer (Wholesale Book Cost):")
    def W_cost(copies): # 'copies' is how many books you bought
        bookPrice = 24.95
        shipFirst = 3
        shipAfter = 0.75
        discount = 0.4
        
        booksTotal = (bookPrice*(1-discount))*copies # flat price of the books
        
        shipCost = shipFirst+(shipAfter*(copies-1)) # value of the shipping cost
        
        total = booksTotal+shipCost # adds the book and shipping costs
        
        print(f"The total wholesale price is ${total:.2f}.\n") # prints the total with only two decimals
    W_cost(60)
    
# Q3
def q3():
    print("Question 3 Answer (Running Time Calculation):")
    def runtime(sHour,sMin):
        paceE = (8*60)+15 # easy pace
        paceT = (7*60)+12 # tempo pace
        totalSec = (paceE*2)+(paceT*3)
        totalMin = totalSec // 60 # gets the minutes
        totalSecs = totalSec % 60 # gets the seconds
        semiTotM = sMin + totalMin
        semiTotH = sHour
        if semiTotM >= 60:
            semiTotH += semiTotM // 60
            semiTotM = semiTotM % 60
        return semiTotH,semiTotM # finalizes the totals for the hour and the minute
    
    semiTotH,semiTotM = runtime(6,52)
    print(f"You will arrive home at {semiTotH}:{semiTotM}.\n") # prints the end time
    
q1()
q2()
q3()
