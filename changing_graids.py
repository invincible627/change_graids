language = input("Select language. Type pe or persian for Persian, and en or english for English\n")
if language.lower() == "en" or language.lower() == "english":
    print("Dear teacher, here you can review and save your student's grades.")
    few_of_students = int(input("Please enter the number of your students\n"))
    few_number = 0
    result_of_students_name = []
    while few_number < few_of_students:
        student_name = input("Enter the student's name\n")
        few_number +=1
        result_of_students_name.append(student_name)
    few_of_graids = int(input("Please enter the number of grades you want to input\n"))
    few_of_numbers_that_should_be_count = 0
    list_of_graids = []
    while few_of_numbers_that_should_be_count < few_of_graids:
        graids = int(input("Please enter the student's grade as a number\n"))
        few_of_numbers_that_should_be_count +=1
        list_of_graids.append(graids)
    numbers_for_lists = 0
    while numbers_for_lists < len(result_of_students_name) and numbers_for_lists < len(list_of_graids):
        print(result_of_students_name[numbers_for_lists], list_of_graids[numbers_for_lists])
        numbers_for_lists +=1
    question = input("Dear teacher, do you want to change any grades? If yes, enter yes in this input box. If no, enter no in this input box\n")
    if question == "no":
        print("Thank you for using the program up to this point and entering your grades.")
    elif question == "yes":
        number_of_student = int(input("Please enter the student number whose grade you want to change\n"))
        minus_student = number_of_student -1
        new_graid = int(input("Please enter the new grade for the student\n"))
        list_of_graids[minus_student] = new_graid
        print(f"The changes were successfully made to the grade of student number {number_of_student}. The new grade for student {result_of_students_name[minus_student]} is {new_graid}.")
elif language.lower() == "pe" or language.lower() == "persian":
    print("سلام معلم عزیز، اینجا میتونید نمرات دانشآموزهاتون رو بررسی کنید، و ذخیره کنید")
    few_of_students = int(input("لطفاً تعداد دانشآموزهاتون رو وارد کنید\n"))
    few_number = 0
    result_of_students_name = []
    while few_number < few_of_students:
        student_name = input("اسم دانشآموز رو وارد کنید\n")
        few_number +=1
        result_of_students_name.append(student_name)
    few_of_graids = int(input("لطفاً تعداد نمراتی که میخواید وارد کنید رو بنویسید\n"))
    few_of_numbers_that_should_be_count = 0
    list_of_graids = []
    while few_of_numbers_that_should_be_count < few_of_graids:
        graids = int(input("لطفاً نمره ی دانشآموز رو به عدد وارد کنید\n"))
        few_of_numbers_that_should_be_count +=1
        list_of_graids.append(graids)
    numbers_for_lists = 0
    while numbers_for_lists < len(result_of_students_name) and numbers_for_lists < len(list_of_graids):
        print(result_of_students_name[numbers_for_lists], list_of_graids[numbers_for_lists])
        numbers_for_lists +=1
    question = input("معلم عزیز، آیا قصد تغییر نمرات را دارید؟ اگر بله، کلمه ی بله را توی این ادیت باکس وارد کنید، اگر خیر، کلمه ی خیر را توی این ادیت باکس وارد کنید\n")
    if question == "خیر":
        print("ممنون که تا اینجا با برنامه همراه بودید، و نمراتتان را نوشتید")
    elif question == "بله":
        number_of_student = int(input("لطفاً شماره ی دانشآموزی که میخواید نمرش رو تغییر بدید وارد کنید\n"))
        minus_student = number_of_student -1
        new_graid = int(input("لطفاً نمره ی جدید دانشآموز رو وارد کنید\n"))
        list_of_graids[minus_student] = new_graid
        print(f"تغییرات با موفقیت روی نمره ی دانش آموز شماره {number_of_student} انجام شد، نمره ی جدید دانشآموز {result_of_students_name[minus_student]} {new_graid}")
else:
    print("invalid language, please restart program again")
    print("زبان وارد شده نادرست است. لطفاً برنامه را دوباره اجرا کنید")