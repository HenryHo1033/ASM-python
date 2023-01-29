import time

sequence = []
t = time.perf_counter()
for i in range(0, 100000001):
    sequence.append(i)

print(f'coast:{time.perf_counter() - t:.8f}s')


def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1

    while left <= right:

        mid = int((left + right) / 2)

        if sequence[mid] > target:

            right = mid - 1

        elif sequence[mid] < target:

            left = mid + 1

        else:

            return mid + 1

    return None


t = time.perf_counter()
result = binary_search(sequence, 99999999)
print(f'coast:{time.perf_counter() - t:.8f}s')

if result is None:

    print("所查詢的元素不在列表內")

else:

    print(f"所查詢的元素在第{result}位")

t = time.perf_counter()
for index, item in enumerate(sequence):

    if item == 99999999:
        break

print(f'coast:{time.perf_counter() - t:.8f}s')