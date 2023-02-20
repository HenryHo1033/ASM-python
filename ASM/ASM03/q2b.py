import time

def spa(N):

    if N == 0:

        return 0

    elif N == 1 or N == 2:

        return 1

    return spa(N - 3) * 2 + spa(N - 2) + spa(N - 1)


for i in range(4, 9):

    time_start = time.perf_counter()
    spa(i)
    print (f"N ={i} Time taken:{time.perf_counter() - time_start:.8f}s")


def spa_iter(N):

    if N == 0:
        return 0

    elif N == 1 or N == 2:

        return 1

    else:

        sum = 0

        for number in range (2, N + 1):

            sum += 4 * number - 9

    return sum


t_iter = time.perf_counter()
spa_iter(10)
print (f"spa_iter() Time taken: {time.perf_counter() - t_iter:.8f}s \n")