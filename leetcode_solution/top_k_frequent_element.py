import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        buckets = [[] for _ in xrange(len(nums) + 1)]
        for i, count in counts.iteritems():
            buckets[count].append(i)
            
        result = []
        for i in reversed(xrange(len(buckets))):
            for j in xrange(len(buckets[i])):
                result.append(buckets[i][j])
                if len(result) == k:
                    return result
        
        return result
        
