num1 = int(input("Please enter a number"))
num2 = int(input("Please enter a number"))
num3 = int(input("Please enter a number"))
if (num1 > num2) and (num1 > num3):
    print("The first number is the largest")
elif (num2 > num1) and (num2 > num3):
    print("The second number is the largest")
elif (num1 == num2) and (num1 == num3):
    print("All the numbers are the same")
elif (num1 > num2) and (num1 == num3):
    print("The first and third are the largest numbers")
elif (num1 > num3) and (num1 == num2):
    print("The first and second are the largest numbers")
elif (num3 > num2) and (num3 == num1):
    print("The third and first are the largest numbers")
elif (num3 > num1) and (num3 == num2):
    print("The third and second are the largest numbers")
else:
    print("The third number is the largest")

