#Purpose :  function spa with integer parameter N

#Written by Kenny Ng Wai Yu
#On 21/2/2023
#For Assignment 3
def spa(N):

    if N == 0:

        return 0

    elif N == 1 or N == 2:

        return 1

    return spa(N - 3) * 2 + spa(N - 2) + spa(N - 1)


print (spa(10))