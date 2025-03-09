import math


class zad10:
    number = 0
    def __init__(self):
        self.number = int(input("Podaj liczbe: "))
        sqrt1 = math.sqrt(self.number)
        if(sqrt1%1 == 0):
            print("Pierwiastek to: ", int(sqrt1))
        else:
            mn = round(sqrt1)
            wi = math.ceil(sqrt1)
            print("Pierwiastek ma wartosc pomiedzy: ", mn, " a ", wi, ".")

    def test(self):
        print(self.number)





nowe = zad10()
nowe.test()
