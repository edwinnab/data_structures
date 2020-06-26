def grade_point_average():
    a = 8
    int(a)
    b = 6
    int(b)
    c = 4
    int(c)
    grades = 1
    while grades <= 3:
        grade_points = (input("Enter your grade: "))
        if grade_points == a:
            print("that is: ", a)
        if grade_points == b:
            print("that is: ",b)
        if grade_points == c:
            print("that is: ",c)
        grades = grades + 1
        average = int(a+b+c)/3
    return average
print("your average is: ", grade_point_average()) 
