print('سلام معلم عزیز، اینجا میتونید نمرات دانشآموزهاتون رو بررسی کنید، و ذخیره کنید')
few_of_students = int(input('لطفاً تعداد دانشآموزهاتون رو وارد کنید\n'))
few_number = 0
result_of_students_name = []
while few_number < few_of_students:
    student_name = input('اسم دانشآموز رو وارد کنید\n')
    few_number +=1
    result_of_students_name.append(student_name)
few_of_graids = int(input('لطفاً تعداد نمراتی که میخواید وارد کنید رو بنویسید\n'))
few_of_numbers_that_should_be_count = 0
list_of_graids = []
while few_of_numbers_that_should_be_count < few_of_graids:
    graids = int(input('لطفاً نمره ی دانشآموز رو به عدد وارد کنید\n'))
    few_of_numbers_that_should_be_count +=1
    list_of_graids.append(graids)
numbers_for_lists = 0
while numbers_for_lists < len(result_of_students_name) and numbers_for_lists < len(list_of_graids):
    print(result_of_students_name[numbers_for_lists], list_of_graids[numbers_for_lists])
    numbers_for_lists +=1
question = input('معلم عزیز، آیا قصد تغییر نمرات را دارید؟ اگر بله، کلمه ی بله را توی این ادیت باکس وارد کنید، اگر خیر، کلمه ی خیر را توی این ادیت باکس وارد کنید\n')
if question == 'خیر':
    print('ممنون که تا اینجا با برنامه همراه بودید، و نمراتتان را نوشتید')
elif question == 'بله':
    number_of_student = int(input('لطفاً شماره ی دانشآموزی که میخواید نمرش رو تغییر بدید وارد کنید\n'))
    minus_student = number_of_student -1
    new_graid = int(input('لطفاً نمره ی جدید دانشآموز رو وارد کنید\n'))
    list_of_graids[minus_student] = new_graid
    print(f'تغییرات با موفقیت روی نمره ی دانش آموز شماره {number_of_student} انجام شد، نمره ی جدید دانشآموز {result_of_students_name[minus_student]} {new_graid}')
# توضیحاتی که از هوش مصنوعی خواستم
# در این کد، چند مرحله مشخص با استفاده از ورودی کاربر، لیست‌ها، حلقه‌ها و شرط‌ها اجرا شده:
# ۱. خوش‌آمدگویی
# با استفاده از print، پیام اولیه برای معلم نمایش داده می‌شه.
# ۲. دریافت تعداد دانش‌آموزها
# با input و تبدیل به int، تعداد دانش‌آموزها گرفته می‌شه و در متغیر few_of_students ذخیره می‌شه.
# ۳. گرفتن نام دانش‌آموزها
# با استفاده از while و شمارنده‌ی few_number، به تعداد مشخص‌شده، نام‌ها از کاربر گرفته می‌شن و در لیست result_of_students_name ذخیره می‌شن.
# ۴. دریافت تعداد نمرات
# دوباره با input و تبدیل به عدد، تعداد نمراتی که باید وارد بشن گرفته می‌شه و در few_of_graids ذخیره می‌شه.
# ۵. گرفتن نمرات
# با while و شمارنده‌ی few_of_numbers_that_should_be_count، نمرات از کاربر گرفته می‌شن و در لیست list_of_graids ذخیره می‌شن.
# ۶. نمایش نام‌ها و نمرات
# با استفاده از while و شمارنده‌ی numbers_for_lists، نام هر دانش‌آموز همراه با نمره‌ی مربوط بهش چاپ می‌شه. شرط حلقه تضمین می‌کنه که از محدوده‌ی لیست‌ها خارج نشه.
# ۷. پرسش درباره‌ی تغییر نمره
# با input، از کاربر پرسیده می‌شه که آیا می‌خواد نمره‌ای رو تغییر بده یا نه.
# ۸. شرط بررسی پاسخ
# اگر پاسخ «خیر» باشه، پیام پایانی چاپ می‌شه.
# اگر «بله» باشه، مراحل زیر انجام می‌شن:
# گرفتن شماره‌ی دانش‌آموز
# کم کردن یک واحد از شماره برای تبدیل به ایندکس لیست
# گرفتن نمره‌ی جدید
# جایگزینی نمره‌ی جدید در لیست نمرات
# چاپ پیام موفقیت‌آمیز تغییر نمره
# در مجموع، این کد با استفاده از ورودی‌های عددی و متنی، لیست‌ها برای ذخیره‌سازی، حلقه‌ها برای تکرار، و شرط‌ها برای تصمیم‌گیری، یک سیستم ساده برای ثبت و ویرایش نمرات دانش‌آموزها طراحی کرده.