
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
        if self.head is None:
            self.head = newNode
            return
        last = self.head

        while last.next:
            last = last.next
        last.next = newNode

def mergeList(head1, head2):
    temp = None
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.next = mergeList(head1.next, head2)

    else:
        temp = head2
        temp.next = mergeList(head1, head2.next)

    return temp

if __name__ == "__main__":
    list1 = linkedList()
    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)

    list2 = linkedList()
    list2.append(5)
    list2.append(15)
    list2.append(18)
    list2.append(35)
    list2.append(80)
    
    list3 = linkedList()

    list.head = mergeList(list1.head, list2.head)
    print("merge linked list is : ", end="")
    list3.printList()

