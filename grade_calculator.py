homework =int(input("enter your homework percent -"))
midterm =int(input("enter your midterm percent -"))
finalexam =int(input("enter your final exams percent -"))
homework = homework * 0.2
midterm = midterm * 0.3
finalexam = finalexam * 0.5
grade = homework + midterm +finalexam
print(grade)
if grade > 75:
    print("you are passed")
else:
    print("you are failed")
