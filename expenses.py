pay = eval(input("Enter your monthly salary "))
rent = eval(input ("Enter your rent"))
utilities = eval(input("Enter your utilities"))
groceries = eval(input("Enter your groceries"))
studentloans = eval(input("Enter your student loans"))

totalbills = rent + utilities + groceries + studentloans
print(totalbills)

discretionary_amount = pay - totalbills
print(discretionary_amount)




