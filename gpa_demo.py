
#welcome the user to the calculator
print("Welcome to the Grade_Point_Average calculator.")
print("Enter a letter grade per line.")
#letter grades
points = {"A+" :4.0, "A" :4.0, "A-" :3.67, "B+" :3.33, "B" :3.0, "B-" :2.67, "C+" :2.33, "C" :2.0, "C-" :1.67, "D+" :1.33, "D" :1.0, "F" :0.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input("Enter your grade: ")
    if grade == "":
        print("blank means you have entered total grade points")
        done = True
    elif grade not in points:
        print("The grade {} you have entered is wrong.".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
#avoids division by zero
if num_courses > 0:
    average = total_points/num_courses
    print("your GPA is : {} ".format(average))
