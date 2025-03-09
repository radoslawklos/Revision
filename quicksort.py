
arr = [12, 5, 82, 2, 4, 1, 54, 7, 13, 9, 8]

def quicksort(arr):
    if(len(arr) <= 1):
        return arr
    piv = arr[len(arr) //2]
    left = []
    right = []
    mid = []
    for i in range(len(arr)):
        if(arr[i] < piv):
            left.append(arr[i])
        if(arr[i] > piv):
            right.append(arr[i])
        if(arr[i] == piv):
            mid.append(arr[i])
    result = left + mid + right
    return quicksort(left) + mid + quicksort(right)

print(quicksort(arr))