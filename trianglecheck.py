x = int(input("Length of side : "))
y = int(input("Length of side : "))
z = int(input("Length of side : "))
a = 0
#check for isosceles triangle
if x == y:
    a = 1
elif z == y:
    a = 1
elif x == z:
    a = 1
#check for equilateral triangle
if x == y == z:
    a = 2
#chech for scalen triangle
if x != y != z:
    a = 3
#check if triangle is a right angled triangle:
if x**2 + y**2 == z**2:
    print("The triangle is a right angled triangle")
elif y**2 + z**2 == x**2:
    print("The triangle is a right angled triangle")
elif x**2 + z**2 == y**2:
    print("The triangle is a right angled triangle")
#check for the sides if triangle can be formed or not
if x+y<=z or x+z<=y or y+z<=x:
    a = 0
#check for which triangle
if a == 0:
    print("With the given sides triangle can't be formed")
elif a == 1:
    print("It is an isosceles triangle")
elif a == 2:
    print("It is an equilateral triangle")
elif a == 3:
    print("It is a scalene triangle")