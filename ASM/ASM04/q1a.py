import timeit
import random

def validate(lst):

    check_value = [500, 1000, 2000, 4000]

    for item in lst:
        if item not in check_value:
            raise Exception(f"數字必須是INT類型的500, 1000, 2000, 4000。目前的數字是{item}", )

def funcA(lst):
    '''
    O(N)
    :param lst:
    :return:
    '''
    return [i**2 for i in lst]

def funcB(lst):
    '''
    O(N log N)
    :param lst:
    :return:
    '''
    return sorted(lst)

def funcC(lst):
    '''
    O(N^2)
    :param lst:
    :return:
    '''

    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

sizes = [500, 1000, 2000, 4000]

validate(sizes)

for size in sizes:
    lst = [random.randint(1, 100) for _ in range(size)]
    time_funcA = timeit.timeit(stmt=f"funcA({lst})", globals=globals(), number=1)
    time_funcB = timeit.timeit(stmt=f"funcB({lst})", globals=globals(), number=1)
    time_funcC = timeit.timeit(stmt=f"funcC({lst})", globals=globals(), number=1)
    print(f"List size: {size}")
    print(f"funcA time: {round(time_funcA, 4)} seconds")
    print(f"funcB time: {round(time_funcB, 4)} seconds")
    print(f"funcC time: {round(time_funcC, 4)} seconds")
    print ()