
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def find_mid(self):
        cnt = 0
        tmp = self.head
        while tmp and tmp.next:
            cnt += 1
            tmp = tmp.next
        cnt = cnt//2
        res = self.head
        for i in range(cnt):
            res = res.next
        return res.data

ll = LinkedList()
for i in range(1,7):
    ll.append(i)
print(ll.find_mid())