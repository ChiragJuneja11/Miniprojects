class Solution:
    def romanToInt(self, s: str) -> int:
        x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        #inti = input()
        inti = s
        total = 0
        x_ = list()
        for i in inti.upper():
            x_.append(x[i])
        #print(x_)
        x_ = x_[::-1]
        #print(x_)
        first = True
        for i in x_:
            if first == True:
                previous = 0
            current = i
            #print(previous)
            if previous>current:
                total=total-current
                previous = current
                first = False
                #print("previous",previous)
                #print("current",current)
            else:
                total+=current
                previous = current
                first = False
                #print("previous",previous)
                #print("current",current)
        return total