class MyQueue(object):
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.B.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        return self.B[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.A and not self.B


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
