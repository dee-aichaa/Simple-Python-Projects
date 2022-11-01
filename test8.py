# studentGr1 = int(input("Please enter your first grade: "))
# studentGr2 = int(input("Please enter your second grade: "))
# studentGr3 = int(input("Please enter your third grade: "))
# while studentGr1 > 0:
#     studentGr1 = int(input("Please enter your first grade: "))
#     if studentGr1 < 0:
#         break
#     else:
#         studentGr2 = int(input("Please enter your second grade: "))
#         studentGr3 = int(input("Please enter your third grade: "))
#         str1 = "Average grade: "
#         total_grade = studentGr1 + studentGr2 + studentGr3
#         average_grade = total_grade/3
#         print(str1,average_grade)
# print(str1,average_grade)
str1 = ("Average: ")
while True:
    st1 = int(input("Please enter the first grade: "))
    if st1 < 0:
        break
    st2 = int(input("Please enter the second grade: "))
    st3 = int(input("Please enter the third grade: "))
    total = st1 + st2 + st3
    average = total/3
    print(str1, average)