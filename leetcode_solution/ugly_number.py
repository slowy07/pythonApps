class Solution(object):
    def isUgly(self, num):
        """
        :type n: int
        :rtype: bool
        """
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i

        return num == 1
