#Calculator to do basic calculations like addition, subtraction, multiplication, division, square root, cube root, calculating power of a numbers and factorial value of a number

def addition(list):
    x = 0.0
    for i in list:
        x = x+float(i)
    return x

def subtraction(x):
    return float(x[0])-float(x[1])

def multiplication(lst):
    product = 1
    for i in lst:
        product = float(i)*float(product)
    return product

def division(x):
    return float(x[0])/float(x[1])

def square_root(x):
    x = pow(float(x),0.5)
    return x

def cube_root(x):
    x = pow(float(x),0.33333333333333333)
    return x

def to_the_powerof(x):
    return pow(float(x[0]),float(x[1]))

def factorial(x):
    factor = 1
    for i in range(1,int(x)+1):
        factor *= i
    return factor

print("Enter a digit from 1 to 8 :")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")
print("5 for square root")
print("6 for cube root")
print("7 for to get the power of x")
print("8 to get a factorial value")

calculate = int(input())




if calculate == 1:
    print(addition(input().split()))
elif calculate == 2:
    print(subtraction(input().split()))
elif calculate == 3:
    print(multiplication(input().split()))
elif calculate == 4:
    print(division(input().split()))
elif calculate == 5:
    print(square_root(input()))
elif calculate == 6:
    print(cube_root(input()))
elif calculate == 7:
    print(to_the_powerof(input().split()))
elif calculate == 8:
    print(factorial(input()))