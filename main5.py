arr1 = [2,4,7,10]
arr2 = [2,3]

def merge(arr1, arr2):
    for i in range(len(arr2)):
        if arr2[i] < max(arr1):
            tmp = max(arr1)
            id1 = arr1.index(tmp)
            arr1[id1] = arr2[i]
            arr2[i] = tmp
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    return arr1, arr2

print(merge(arr1, arr2))
print("test")