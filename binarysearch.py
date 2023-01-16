class binarySearch():

    def binary (arr, 1, r, x):

        if r >=1:

            mid = int(1+ (r - 1) / 2)
            if arr[mid] == x:
                return mid

        elif arr[mid] > x:
            return binarySearch(arr, 1, mid-1, x)

        else:
            return binarySearch(arr, mid+1, r, x)

            else:
                return -1

    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binary(arr, 0, len(arr)-1, x)

    if result != -1:
        print ("元素在數組中的索引為  %d" % result )

    else:
        print ("元素不在數組中")