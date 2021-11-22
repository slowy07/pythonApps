class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        sums = 0
        min_size = float("inf")
        for i in xrange(len(nums)):
            sums += nums[i]
            while sums >= s:
                min_size = min(min_size, i - start + 1)
                sums -= nums[start]
                start += 1
        
        return min_size if min_size != float("inf") else 0
