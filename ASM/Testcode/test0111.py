n = int(input("Enter an integer greater than 3: "))
isPrime = True
k = 2
q = n

while k <= n // 2:
    if n % k == 0:
        isPrime = False
        q = n // k
        break
    k += 1

if isPrime:
    print(f"{n} is a prime number.")
else:
    print(f"The prime factors of {n} are: [{k},", end="")

    k = 2  # 修正：將 k = 2 放在第二個迴圈的外面

    while k <= q:
        if q % k == 0:
            q = q // k
            if q > 1:
                print(", ", end="")
        else:
            k += 1

    print("].")