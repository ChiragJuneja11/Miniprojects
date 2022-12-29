#write a code that will return the highest prime number in current range
n = 10000#int(input("Enter the end of range here :"))
lst=list ()
for i in range (0,n+1):
    if i > 1:
        for z in range (2,i):
        #check for prime or not
            if i%z ==0:
                break
        else:
            lst.append(i)
print (lst[len(lst)-1])
print(lst)