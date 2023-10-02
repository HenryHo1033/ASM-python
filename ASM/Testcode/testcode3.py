size = int(input('Enter the size pattern: '))
for row in range(size):
    for col in range(size):
        if row in (0, size -1) or col in (0,size-1):
            print('*', end='')
        else:
            print(' ',end='')
    print()