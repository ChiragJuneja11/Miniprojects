from random import randint
#passlen = int(input("Enter length of your password : "))
passlen = 5

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_" #total elements = 72
lst = list()

for x in alpha:
    lst.append(x)
lst_ = list()

for n in range(0,passlen+1):
    lst_.append(randint(0,73))

password = list()

for i in lst_:
    password.append(lst[i])
finalpass = "".join(password)

print(finalpass)