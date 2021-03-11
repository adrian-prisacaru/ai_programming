names_input = input('Enter names separated by comma:')
assignments_input = input('Enter assignments separated by comma:')
grades_input = input('Enter grades separated by comma:')

names = names_input.split(',')
assignments = assignments_input.split(',')
grades = grades_input.split(',')


def potential_grade(current_grade, missing_assignments):
    return int(current_grade) + (2 * int(missing_assignments))


# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

for i, name in enumerate(names):
    grade = grades[i]
    assignment = assignments[i]
    print(message.format(name, assignment, grade, potential_grade(grade, assignment)))
