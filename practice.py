amount = float(input("Please enter amount:  "))
for num_people in range(1,20):
    print(f"{num_people} people: ${amount/num_people:,.2f} each")

for n in range(3):
    print("Python")


for n in range(10, 20):
    print(n*n)

for l in "Python":
    print("Python")

word = "Wesh"
i = 0
while i < len(word):
    print(word[i])
    i = i + 1

for n in word:
    print(n)

pword = input("Enter your username:  ")
username = input("Enter your password: ")
str1 = ("Welcome")
while pword != "cat665" and username != "idemba":
    print("Incorrect username and password!")
    username = input("Please try username again: ")
    pword = input("Please try password again: ")
print(str1)



