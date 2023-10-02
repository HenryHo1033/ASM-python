s = input("Enter an integer between 0 and 999: ")
n = int(s)

r1 = n % 10
q1 = n // 10

r2 = q1 % 10
q2 = q1 // 10

result = r1 + r2 + q2

print(f"sum of digits of {n}")
print(f"= {q2} + {r2} + {r1}")
print(f"{result}")