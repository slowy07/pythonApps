class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        op = {"*": lambda x, y: float(x) * y, "/": lambda x, y: float(x) / y}

        stack, tot, prevOp = [0], 0, "+"
        for j, char in enumerate(s):
            if char.isdigit():
                tot = tot * 10 + int(char)
            if j == len(s) - 1 or not char.isdigit() and char != " ":
                if prevOp in ["/", "*"]:
                    calc = op[prevOp](stack[-1], tot)
                    stack[-1] = int(math.floor(calc) if calc > 0 else math.ceil(calc))
                else:
                    stack.append(-tot if prevOp == "-" else tot)

                tot, prevOp = 0, char

        return sum(stack)
