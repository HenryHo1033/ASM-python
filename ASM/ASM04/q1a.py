import timeit


def validate(lst):
    '''
    Check number type
    '''
    for item in lst:
        if item not in [500,1000,2000,4000]:
            raise Exception("List只能是INT type中的500、1000、2000、4000")

def funcA(lst):
    '''
    Big-O of Implementation
    of the Procedure
    O(N)
    '''

    return [i * 2 for i in lst]



def funcB(lst):

    '''
    Big-O of Implementation
    of the Procedure
    O(N^2)
    '''
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    return lst

def funcC(lst):

    '''
    mystery functions
    '''


# Define the list sizes to test
list_sizes = [500, 1000, 2000, 4000]

# Time the execution of each function for each list size
times = {'funcA': [], 'funcB': [], 'funcC': []}

validate(list_sizes)
for size in list_sizes:
    lst = list(range(size))

    # Time funcA
    time = timeit.timeit('funcA(lst)', globals=globals(), number=100)
    times['funcA'].append(round(time, 4))

    # Time funcB
    time = timeit.timeit('funcB(lst)', globals=globals(), number=100)
    times['funcB'].append(round(time, 4))

    # Time funcC
    #time = timeit.timeit('funcC(lst)', globals=globals(), number=10)
    #times['funcC'].append(round(time, 4))
