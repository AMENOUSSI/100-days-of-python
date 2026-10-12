student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
# looping through student score dictionary
for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        grade = "Outstanding"

    elif score >= 81:
        grade = "Exceeds Expectations"

    elif score >= 71:

        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade

print(student_grades)
