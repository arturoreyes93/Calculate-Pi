import random
import math

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

    print ("inside = " + str(inside_throws))
    print("total = " + str(total_throws))

    return calc_pi
