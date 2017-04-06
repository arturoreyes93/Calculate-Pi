#  File: CalculatePI.py

#  Description: calculates the value of PI using the dart board approach and outputs a column with the calculated value and the difference to the real one starting at 100 hundreds shots and ending at 10000000

#  Student Name: Arturo Reyes Munoz

#  Student UT EID: ar48836

#  Course Name: CS 303E

#  Unique Number: 56865

#  Date Created: 03/02

#  Date Last Modified: 03/02

import math
import random

def computePI( numThrows ):

    total_throws = 1
    inside_throws = 0

    while total_throws <= numThrows :

        x = random.uniform(-1.0,1.0)
        y = random.uniform(-1.0,1.0)

        h = math.hypot(x,y)

        if h<1 :

            inside_throws += 1

        total_throws += 1

    calc_pi = 4*(inside_throws / total_throws)

    return calc_pi


def main():

    num = 100

    while num <= 10000000:

        calc_pi = computePI(num)

        diff = (calc_pi) - (math.pi) 

        if diff>0 :
            sign = " +"

        elif diff<0 :
            sign = " "

        else:

            print("wow, exactly the same")

        a = "num = " + str(num)
        b = "  Calculated PI = " + str(round(calc_pi,6))
        c = "  Difference = " + str(sign) + str(round(diff,6))

        if num == 100:
            print(a, end = "      ")

        elif num == 1000:
            print(a, end = "     ")

        elif num == 10000:
            print(a, end = "    ")

        elif num == 100000:
            print(a, end = "   ")

        elif num == 1000000:
            print(a, end = "  ")

        elif num == 10000000:
            print(a, end = " ")

        
        print(b,c)

        num *= 10
    


main()
