class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def getPrefix(pattern):
            prefix = [-1] * len(pattern)
            j = -1
            for i in xrange(1, len(pattern)):
                while j > -1 and pattern[j + 1] != pattern[i]:
                    j = prefix[j]
                if pattern[j + 1] == pattern[i]:
                    j += 1
                prefix[i] = j
            return prefix
        
        if not s:
            return s

        A = s + '#' + s[::-1]
        return s[getPrefix(A)[-1] + 1:][::-1] + s
