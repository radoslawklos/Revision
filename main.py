arr = [5, 3, 4]
win = []

def findIndexes(arr, sumValue):
    allSubs = []
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            sub = arr[i:j+1]
            allSubs.append(sub)
    for i in range(len(allSubs)):
        if(sum(allSubs[i]) == sumValue):
            win.append(allSubs[i])
            cnt += 1
    if(cnt == 0):
        return -1
    result = []
    for i in range(len(win[0])):
        result.append(arr.index(win[0][i])+1)
        result = [result[0], result[len(result)-1]]
    return(result)
print(findIndexes(arr, 2))