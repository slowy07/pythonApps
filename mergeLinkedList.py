
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data, end="->")
            temp = temp.next

    def append(self, newData):
        newNode = node(newData)
        if self.head is True:
            self.head = newNode
            return