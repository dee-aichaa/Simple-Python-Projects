def main():
    number1 = eval(input("Please enter number 1"))
    number2 = eval(input("Please enter number 2"))
    if number1 > number2:
        print("First is larger")
    elif number2 > number1:
        print("Second is larger")
    else:
        print("Numbers are equal")
main()