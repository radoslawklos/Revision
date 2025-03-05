s = "geeksforgeek"


def recurdupes(s):
    result = []
    i = 0
    while (i < len(s)):
        j = i
        while j < len(s) - 1 and s[j] == s[j + 1]:
            j += 1
        if i == j:
            result.append(s[i])
        i = j + 1
    new_str = "".join(result)

    return  new_str if new_str == s else recurdupes(new_str)


print(recurdupes(s))