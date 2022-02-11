import collections


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        lookup = {}
        for i, word in enumerate(words):
            lookup[word] = i

        for i in xrange(len(words)):
            for j in xrange(len(words[i]) + 1):
                prefix = words[i][j:]
                suffix = words[i][:j]
                if prefix == prefix[::-1] and \
                   suffix[::-1] in lookup and lookup[suffix[::-1]] != i:
                    res.append([i, lookup[suffix[::-1]]])
                if j > 0 and suffix == suffix[::-1] and \
                   prefix[::-1] in lookup and lookup[prefix[::-1]] != i:
                    res.append([lookup[prefix[::-1]], i])
        return res
      
