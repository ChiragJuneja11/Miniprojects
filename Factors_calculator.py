x = 100 #int(input("Enter a number for which you want factors : "))
factors = list()
for n in range(1,x+1):
    if ( x%n ) == 0 :
        factors.append(n)
print(factors)