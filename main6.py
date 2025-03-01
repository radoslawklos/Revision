s = "AAA"

def permu(word):
    chars = list(word)
    pers = []
    for i in range(len(chars)):
        for j in range(len(chars)):
            if(i != j):
                for k in range(len(chars)):
                    if(i != k and j != k):
                        str_tmp = chars[i] + chars[j] + chars[k]
                        if(str_tmp not in pers):
                            pers.append(str_tmp)
    return pers


print(permu(s))