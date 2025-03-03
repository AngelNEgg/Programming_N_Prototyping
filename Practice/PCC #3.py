def do_twice(x,y):
    x("spam")
    y('spam')
    
def print_twice(x):
    print(x)
    print(x)
    
def do_four(y):
    print_twice(y)
    print_twice(y)
    
do_twice(print_twice,do_four)
