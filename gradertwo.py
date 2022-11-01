def main():
    testscore_1 = eval(input("Please enter, testscore_1: "))
    testscore_2 = eval(input("Please enter, testscore_2: "))
    exams_score = eval(input("Please enter exams_score: "))
    is6a = ("This is your total score: ")

    final_test1 = testscore_1/100*25
    final_test2 = testscore_2/100*25
    final_exam = exams_score/100*50
    total_score = final_test1 + final_test2 + final_exam
    print(is6a, total_score)

    if total_score < 30:
        print("Repeat course")
    elif total_score > 80:
        print("Grade A")
    elif total_score < 80 and total_score  >= 70:
        print("Grade B")
    elif total_score < 70 and total_score >= 60:
        print("Grade C")
    elif total_score < 60 and total_score >= 50:
        print("Grade D")
    elif total_score < 50 and total_score >= 40:
        print("Grade E")
    else:
        print("Grade F") 
main()