width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

for i in range(height):
    for j in range(width):
        print("*", end=" ")
    print()