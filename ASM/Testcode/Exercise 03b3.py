e1 = int(input("Enter the 1st edge: "))
e2 = int(input("Enter the 2nd edge: "))
e3 = int(input("Enter the 3rd edge: "))

if (e1 + e2 > e3 ) and (e1 + e3 > e2) and (e3 + e2 > e1):
    print(f"Yes! Edges  {e1}, {e2}, and {e3} are able to form a triangle.")
else:
    print(f"Edges {e1}, {e2}, and {e3} CANNOT form a triangel.")