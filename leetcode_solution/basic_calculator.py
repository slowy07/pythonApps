class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sum = 0
        sign = 1
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                res = 0
                while i < len(s) and s[i].isdigit():
                    res = res * 10 + int(s[i])
                    i += 1
                i -= 1
                sum += res * sign
                sign = 1
            elif ch == "-":
                sign *= -1
            elif ch == "(":
                stack.append(sum)
                stack.append(sign)
                sum = 0
                sign = 1
            elif ch == ")":
                sum *= stack.pop()
                sum += stack.pop()
            i += 1
        # For Handling 32-bit Integers...
        if sum <= (1 << 31):
            return sum
        return (1 << 31) - 1
