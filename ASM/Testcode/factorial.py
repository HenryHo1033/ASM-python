n = int(input("Enter a natural number: "))

if n < 0:
    print("Factorial doesn't exist for negative numbers!")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    print(f"The factorial of {n} = ", end="")

    for i in range(n, 0, -1):
        factorial *= i
        if i != n:
            print(" x ", end="")
        print(i, end="")

    print(f" = {factorial}")