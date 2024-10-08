# Wrong ---------------------------------------------

answer = find_rect_area(4,7)
print(answer)

def find_rect_area(w,l):
    area = w*l
    (print("Calculating Area..."))

# Correct ---------------------------------------------

def find_rect_area(w,l):
    area = w*l
    print("Calculating Area...")
    return area

answer = find_rect_area(4,7)
print(answer)
