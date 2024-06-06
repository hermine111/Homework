#6. Tuple Exercise:
#Create a tuple of student names and their corresponding scores. Write a function to find
#the student with the highest score.

def find_student_with_highest_score(students):
    max_score = -1
    top_student = None

    for student, score in students:
        if score > max_score:
            max_score = score
            top_student = student
    return top_student


print(find_student_with_highest_score((("Anna",90), ("Jane", 70), ("Sara", 100))))
