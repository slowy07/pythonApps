import collections


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l, r = [], []
        if len(s) < 10:
            return []
        for i in range(len(s) - 9):
            l.extend([s[i : i + 10]])
        return [k for k, v in collections.Counter(l).items() if v > 1]
