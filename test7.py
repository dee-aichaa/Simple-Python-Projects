Name = input("Please enter your name: ")
Average = int(input("Please enter your average score: "))
GPA = float(input("Please enter youur GPA score: "))
str1 = "Name"
str2 = "Average score"
str3 = "GPA"
while Average != 0:
    if Average > 60 and GPA >= 3.6:
        print(str1,Name,str2, Average,str3, GPA)
    else:
        print("No student detected")
    Name = input("Please enter your name: ")
    Average = int(input("Please enter your average score: "))
    GPA = float(input("Please enter youur GPA score: "))
        
