from operator import index

arr = [2, 3, 4]
tmp = []

def countTrip(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if(i != j):
                for k in range(len(arr)):
                    if(i != k):
                        if(arr[i] + arr[j] == arr[k]):
                            cnt += 1
                            tmp.append([arr[i], arr[j], arr[k]])
    return cnt

print("There are: " , countTrip(arr) , " triplets.")
print(tmp)