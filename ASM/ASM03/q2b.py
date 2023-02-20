import time

def spa(N):

    if N == 0:

        return 0

    elif N == 1 or N == 2:

        return 1

    return spa(N - 3) * 2 + spa(N - 2) + spa( N - 1)


t4 = time.perf_counter()
print (spa(4))
print (f"Time taken: {time.perf_counter() - t4:.8f}s \n")

t5 = time.perf_counter()
print (spa(5))
print (f"Time taken: {time.perf_counter() - t5:.8f}s \n")

t6 = time.perf_counter()
print (spa(6))
print (f"Time taken: {time.perf_counter() - t6:.8f}s \n")

t7 = time.perf_counter()
print (spa(7))
print (f"Time taken: {time.perf_counter() - t7:.8f}s \n")

t8 = time.perf_counter()
print (spa(8))
print (f"Time taken: {time.perf_counter() - t8:.8f}s \n")


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
print (spa_iter(10))
print (f"Time taken: {time.perf_counter() - t_iter:.8f}s \n")