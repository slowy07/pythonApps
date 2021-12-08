class Node(object):
    def __init__(self, value):
        super(Node, self).__init__()

        self._value = value
        self._next = None

    def traverse(self):
        node = self
        while node:
            print(node._value)
            node = node._next


node_1 = Node(234)
node_2 = Node("bcd")
node_3 = Node("linked list")

node_1._next = node_2
node_2._next = node_3
