# Angel Nazaire
# 3/7/2025
# Period 5-6
'''Python Code Challenge #5: '''

def check_fermat(a,b,c,n):
  ans1 = a**n
  ans2 = b**n
  ans3 = c**n
  if n>2 and (ans1+ans2) == ans3:
    print("Holy smokes, Fermat was wrong!")
  else:
    print("No, that doesn't work.")

check_fermat(8,6,3,2)
