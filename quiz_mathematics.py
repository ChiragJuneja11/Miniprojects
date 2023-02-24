import numpy as np
def easy(): #easy questions that can be solved by any person without much difficult calculations
    a,b = np.random.randint(1,10000),np.random.randint(1,10000)
    Z = np.random.randint(1,4)
    if  Z == 1:
        print(a,"+",b)
            #additionn question

    elif Z == 2:
        if a>b:
            print(a,"-",b)
        elif a<b:
            print(b,"-",a)
            #subtraction questions

    elif Z == 3:
        A = [300,600,1200,2400,3000]
        B = [2,3,4,5,6,12,25,50,60,100,150]
        x = A[np.random.randint(0,5)]
        y = B[np.random.randint(0,11)]
        print(x,"/",y)
            #division question
        
    elif Z == 4:
        x = 40320
        y = np.random.randint(2,8)
        print(x,"*",y)
        #multiplication question


print("This is a small quiz game that contains 10 questions each game \n " 
      "The questions will be completely random and will be non repetetive"
      )
#Continue = str(input("Enter Yes to start :")).lower()
Continue = "yes"
if Continue == "yes":
    for i in range(100):
        easy()