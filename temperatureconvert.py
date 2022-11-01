#convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Isatou Demba

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = (9/5) * celsius + 32
    print("The temperature is ",fahrenheit," degrees Fahrenheit.")

main()

def spamneggs():
   spam, eggs = eval(input("Enter # of slices of spam followed by # of eggs: "))
   print ("You ordered", eggs, "eggs and", spam, "slices of spam. Yum!")

spamneggs()