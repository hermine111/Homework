
# Exercise 8: Find student with highest average score
# Write a function that takes a dictionary with information about students. Return info
# about the student with highest average score
# Dictionary example
# students_info = {
# 'student1': {
# 'name': 'John Doe',
# 'age': 20,
# 'subjects': ['Math', 'Physics', 'English'],
# 'scores': [7, 9, 9, 6],
# },
# 'student2': {
# 'name': 'Jane Smith',
# 'age': 19,
# 'subjects': ['Chemistry', 'Biology', 'History'],
# 'scores': [5, 6, 8, 10],
# },
# 'student3': {
# 'name': 'Bob Johnson',
# 'age': 21,
# 'subjects': ['Computer Science', 'Statistics', 'Psychology'],
# 'scores': [8, 8, 9, 9, 9],
# },
# }


def calculate_average(scores):
    total_score = 0
    for score in scores:
        total_score += score
    return total_score/len(scores)


def student_with_highest_average_score(students_info):
    highest_average_score = -1
    student_with_highest_average = None

    for student, info in students_info.items():
        average_score = calculate_average(info['scores'])
        if average_score > highest_average_score:
            highest_average_score = average_score
            student_with_highest_average = info
    return student_with_highest_average


print(student_with_highest_average_score(students_info = {
'student1': {
'name': 'John Doe',
'age': 20,
'subjects': ['Math', 'Physics', 'English'],
'scores': [7, 9, 9, 6],
},
'student2': {
'name': 'Jane Smith',
'age': 19,
'subjects': ['Chemistry', 'Biology', 'History'],
'scores': [5, 6, 8, 10],
},
'student3': {
'name': 'Bob Johnson',
'age': 21,
'subjects': ['Computer Science', 'Statistics', 'Psychology'],
'scores': [8, 8, 9, 9, 9],}}))


