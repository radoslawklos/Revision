
arr = [10]

def zad14(arr):
    arr = sorted(arr)
    final_cost = 0
    if(len(arr) < 2):
        return 0
    while len(arr) > 1:
        tmp = arr[0] + arr[1]
        final_cost += tmp
        arr.remove(arr[0])
        arr.remove(arr[0])
        arr.append(tmp)
        arr = sorted(arr)
    return (final_cost)

print(zad14(arr))
