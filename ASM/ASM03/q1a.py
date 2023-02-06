import random

def validate(N):

    assert N > 0

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