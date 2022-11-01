import random
correctAnswer = 0
st1 = ("Number of correct answers")
for x in range(5):
    q1 = int(random.random()*10)
    q2 = int(random.random()*10)
    user_ans = eval(input(f"What is {q1} + {q2}? "))
    ans1 = q1 + q2
    if user_ans == ans1:
        print("Correct answer ;)")
        correctAnswer = correctAnswer + 1 
    else:
        print("Wrong answer!")
print(st1,correctAnswer)
