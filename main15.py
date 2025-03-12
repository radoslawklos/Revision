arr = (-8, 2, 3, -6, 10)
k = 2

def zad15():
    for i in range(len(arr)):
        tmp = []
        if(i + k <= len(arr)):
            for j in range(k):
                tmp.append(arr[i+j])
            for j in range(len(tmp)):
              if(tmp[j] < 0):
                  print("Dla grupy: ", tmp, " pierwsza ujemna to: ", tmp[j])
                  break
              if(j == k-1):
                  print("Dla grupy: ", tmp, " nie ma ujemnych")
zad15()