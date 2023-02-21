#Purpose :  Turn the above into a recursive function.

#Written by Kenny Ng Wai Yu
#On 21/2/2023
#For Assignment 3

import  time

def find_pi_square(N):

    try:
        assert N > 0
    except:
        raise Exception("N must be > 0")

    N = int (N)

    if N == 1:

        return 8

    else :

        return 8 / pow(N * 2 - 1, 2) + find_pi_square(N - 1)


print (find_pi_square(1))
print (find_pi_square(7))
print (find_pi_square(0))