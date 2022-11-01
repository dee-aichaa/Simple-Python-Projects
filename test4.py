Grade1 = eval(input("Please enter the first grade out of 100: "))
Grade2 = eval(input("Please enter the second grade out of 100: "))
Grade3 = eval(input("Please enter the second grade out of 100: "))
total_score = Grade1 + Grade2 + Grade3
average_score = (total_score/3)
str1 = "Total score"
str2 = "Average score"
print(str1, total_score, str2, average_score)
if average_score >= 60:
    print("You've passed ;) Well done!!")
else:
    print("You've failed :( Better luck next time.")

