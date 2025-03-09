arr = [[7, 8], [1, 5], [2, 4], [4, 6]]

def mergeInter(arr):
    arr.sort(key=lambda x: x[0])

    res = [arr[0]]
    for i in range(1, len(arr)):
        prev_s, prev_e = res[-1]
        curr_s, curr_e = arr[i]

        if curr_s <= prev_e:
            res[-1] = [prev_s, max(prev_e, curr_e)]
        else:
            res.append([curr_s, curr_e])
    return res


print(mergeInter(arr))