arr = [4, 3, 2, 1]

def invCount():
    final_sum = 0
    sum = 0
    for i in range(1, len(arr)):
        if(arr[i] < arr[i-1]):
            sum += i
            if(sum > final_sum):
                final_sum = sum
        else:
            sum = 0
    print(final_sum)

invCount()