n = 9  # 長方形的寬度,也是數字的範圍

for i in range(1, n + 1):
    if i % 2 == 0:
        numbers = range(1, n+1, 1)  # 從 1 開始倒數到 n
    else:
        numbers = range(n, 0, -1)  # 從 n 開始數到 1

    for j in numbers:
        print(j, end="")

    print()  # 換行
