arr = [2, 3, -8, 7, -1, 2, 3]

def findMaxSum(arr):
    allSubs = []
    max =   arr[0]
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            sub = arr[i:j+1]
            allSubs.append(sub)
    for i in range(len(allSubs)):
        if(sum(allSubs[i]) > max):
            max = sum(allSubs[i])
            result = allSubs[i]
    return result

print(findMaxSum(arr))
print(" ", sum(findMaxSum(arr)))