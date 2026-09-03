student_details= {
    "name_1": "priya",
    "marks_1": 85,
    "name_2": "ravi",
    "marks_2": 90,
    "name_3": "siya",
    "marks_3": 78
}
max = 0
print(f"student name is {student_details['name_1']} and marks of the student is {student_details['marks_1']}")
print(f"student name is {student_details['name_2']} and marks of the student is {student_details['marks_2']}")
print(f"student name is {student_details['name_3']} and marks of the student is {student_details['marks_3']}") 
for key in student_details:
    if key.startswith("marks"):
        if student_details[key] > max:
            max = student_details[key]
print(max)