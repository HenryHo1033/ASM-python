#Purpose : Generates and return a list of random integers in the range 1 to 100 (both inclusive).

#Written by Kenny Ng Wai Yu
#On 21/2/2023
#For Assignment 3
import random

def validate(N):
    try:
        assert N > 0
    except:
        raise ValueError("N must > 0.")

def genRanNumList(N):

    validate(N)
    random_list = []

    for i in range(N):

        random_list.append(random.randint(1,100))

    return random_list


print (genRanNumList(10))
print (genRanNumList(20))
print (genRanNumList(30))
print (genRanNumList(0))