n = int(input("Enter an integer: "))
if n % 5 == 0:
    print(n, "is divisible by 5.")
else:
    print(n, "is NOT divisible by 5.")
if n % 6 ==0:
    print(n, "is divisible by 6.")
else:
    print(n, "is NOT divisible by 6.")
if n % 5 == 0 and n % 6 ==0:
    print(n, "is divisible by 5 and 6.")
else:
    print(n, "is NOT divisible by 5 and 6.")