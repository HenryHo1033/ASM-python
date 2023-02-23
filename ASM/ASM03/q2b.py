#Purpose :  recursive way of finding spaghetti numbers

#Written by Kenny Ng Wai Yu
#On 21/2/2023
#For Assignment 3

import time

def spa(N):

    if N == 0:

        return 0

    elif N == 1 or N == 2:

        return 1

    return spa(N - 3) * 2 + spa(N - 2) + spa(N - 1)


def spa_iter(N):
    spa_list = [0, 1, 1]

    if N == 0:
        return spa_list[N]

    elif N == 1 or N == 2:

        return spa_list[N]

    else:

        for number in range (3, N + 1):

            spa_list.append(spa_list[number - 3] * 2 + spa_list[number - 2] + spa_list[number - 1])

    return spa_list[N]


for i in range(4, 9):

    time_start = time.perf_counter()
    spa(i)
    print(f"spa({i}) Time taken:{time.perf_counter() - time_start:.8f}s")

    time_start = time.perf_counter()
    spa_iter(i)
    print (f"spa_iter({i}) Time taken:{time.perf_counter() - time_start:.8f}s\n")