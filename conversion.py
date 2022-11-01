#Research current rates of monetary exchange. 
# Write the program that allows the user to enter 
# an amount of dalasis and convert it to Euros 
# and dollars.
# by: Isatou Demba

dalasis = eval(input("Please enter your amount"))
str1 = ("Dollars")
str2 = ("Euros")
dollars = dalasis//52.00
euros = dalasis//60.35
print("Conversion =",dollars,str1,"or",euros,str2)


