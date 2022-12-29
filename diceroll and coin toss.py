import random
import numpy as np

def errhandle():
    print("You incurred an error start again or stop the current program")
def coin_toss():
    choices = ["Heads","Tails"]
    times = int(input("Enter no. of times coin is tossed : "))
    head = 0
    tail = 0
    for n in range(0,times):
        result = np.random.choice(choices)
        if result == "Heads":
            head += 1
        elif result == "Tails":
            tail += 1
    print("No. of head is", head,"and tails is",tail,".")
    #print("Probability will be : ",head/times)
coin_toss()

def dice_roll():
    choices = [1,2,3,4,5,6]
    times = int(input("Enter no. of dices rolled together : "))
    if times>5:
        chk = int(input("Enter the number on side of dice for probabilty check :"))
        if chk > 6:
            errhandle()
        cnt = 0
    roll = list()
    for n in range(0,times):
        result = np.random.choice(choices)
        roll.append(result)
        if times>5:
            if result == chk:
                cnt += 1
    if times < 5:
        print("Dice roll gives",roll,"and sum is",sum(roll),".")
    else:
        print("Probability will be :",cnt/times,"and it came",cnt,"times")
dice_roll()