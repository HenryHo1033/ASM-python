import time

def spa(N):

    if N == 0:

        return 0

    elif N == 1 or N == 2:

        return 1

    return spa(N - 3) * 2 + spa(N - 2) + spa( N - 1)


print (spa(4))
print (f"Time taken: {time.perf_counter()}s \n")

print (spa(5))
print (f"Time taken: {time.perf_counter()}s \n")

print (spa(6))
print (f"Time taken: {time.perf_counter()}s \n")

print (spa(7))
print (f"Time taken: {time.perf_counter()}s \n")

print (spa(8))
print (f"Time taken: {time.perf_counter()}s \n")