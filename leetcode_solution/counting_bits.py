class Solution(object):
    def countBits(self, num):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in xrange(1, num + 1):
            res.append((i & 1) + res[i >> 1])
        return res
        
