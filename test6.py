name = input("Please enter your name: ")
iD_num = int(input("Please enter the ID number: "))
numBed = int(input("Please enter the number of bedrooms: "))
str1 = "Name: "
str2 = "ID No. "
str3 = "Commission earned on rental: "
if numBed == 3:
    commission1 = "$100"
    print(str1,name,str2,iD_num,str3,commission1)
elif numBed == 2:
    commission2 = "$75"
    print(str1,name,str2,iD_num,str3,commission2)
elif numBed == 1:
    commission3 = "$55"
    print(str1,name,str2,iD_num,str3,commission3)
elif numBed == 0:
    commission4 = "$30"
    print(str1,name,str2,iD_num,str3,commission4)
else:
    print("Sorry, room is not available")