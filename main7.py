s = "geeksforgeek"
czy = False

def recurdupes(s):
    for i in range(1,len(s)):
        if(s[i] == s[i-1]):