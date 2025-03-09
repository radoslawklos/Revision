class NextGreat:
    arr = [6, 8, 0, 1, 3]
    def __init__(self):
        tmp = self.arr.sort()
        for i in range(len(self.arr) - 1):
            print("For integer: ", self.arr[i], " larger is: ", self.arr[i+1])
        print("For integer: ", self.arr[len(self.arr)-1], "there is no larger number")


NextGreat()
