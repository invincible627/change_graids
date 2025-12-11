print('Dear teacher, here you can review and save your students\' grades.')
few_of_students = int(input('Please enter the number of your students\n'))
few_number = 0
result_of_students_name = []
while few_number < few_of_students:
    student_name = input('Enter the student\'s name\n')
    few_number +=1
    result_of_students_name.append(student_name)
few_of_graids = int(input('Please enter the number of grades you want to input\n'))
few_of_numbers_that_should_be_count = 0
list_of_graids = []
while few_of_numbers_that_should_be_count < few_of_graids:
    graids = int(input('Please enter the student\'s grade as a number\n'))
    few_of_numbers_that_should_be_count +=1
    list_of_graids.append(graids)
numbers_for_lists = 0
while numbers_for_lists < len(result_of_students_name) and numbers_for_lists < len(list_of_graids):
    print(result_of_students_name[numbers_for_lists], list_of_graids[numbers_for_lists])
    numbers_for_lists +=1
question = input('Dear teacher, do you want to change any grades? If yes, enter "yes" in this input box. If no, enter "no" in this input box\n')
if question == 'no':
    print('Thank you for using the program up to this point and entering your grades.')
elif question == 'yes':
    number_of_student = int(input('Please enter the student number whose grade you want to change\n'))
    minus_student = number_of_student -1
    new_graid = int(input('Please enter the new grade for the student\n'))
    list_of_graids[minus_student] = new_graid
    print(f'The changes were successfully made to the grade of student number {number_of_student}. The new grade for student {result_of_students_name[minus_student]} is {new_graid}.')
# Explanations requested from AI
# In this code, several specific steps are executed using user input, lists, loops, and conditions:
# 1. Greeting
# A welcome message is displayed to the teacher using print.
# 2. Get the number of students
# The number of students is obtained using input and converted to int, stored in few_of_students.
# 3. Get student names
# Using a while loop and counter few_number, the specified number of names are taken from the user and stored in the result_of_students_name list.
# 4. Get the number of grades
# Again, using input and converting to number, the number of grades to be entered is obtained and stored in few_of_graids.
# 5. Get grades
# Using a while loop and counter few_of_numbers_that_should_be_count, grades are obtained from the user and stored in the list_of_graids list.
# 6. Display names and grades
# Using a while loop and counter numbers_for_lists, each student's name along with their corresponding grade is printed. The loop condition ensures it doesn't go out of the lists' bounds.
# 7. Ask about changing a grade
# Using input, the user is asked if they want to change a grade or not.
# 8. Check the response condition
# If the response is "no", the final message is printed.
# If "yes", the following steps are performed:
# - Get the student number
# - Subtract one unit from the number to convert to list index
# - Get the new grade
# - Replace the new grade in the grades list
# - Print a successful change message
# Overall, this code uses numeric and text inputs, lists for storage, loops for repetition, and conditions for decision-making to design a simple system for recording and editing student grades.