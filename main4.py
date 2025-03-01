arr = [1]


def missing(arr):
    size = len(arr)
    tmp = 0
    if(len(arr) <= 1):
        print("It's just 1, 2 is missing.")
        return 2
    for i in range(1, size + 1):
        if(i not in arr):
            print("Brakuje: ", i)
            tmp = i
    return tmp

missing(arr)