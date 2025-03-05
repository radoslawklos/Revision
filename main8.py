s = "geeksforgeeks"

def longDist(s):
    list_tmp = []
    list_res = []
    for i in range(len(s)):
        if (s[i] in list_tmp):
            list_tmp.clear()
            list_tmp.append(s[i])
        else:
            list_tmp.append(s[i])
            if(len(list_res) < len(list_tmp)):
                list_res = list_tmp.copy()
    return str(list_res)


print(longDist(s))