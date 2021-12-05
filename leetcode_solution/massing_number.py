class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(xrange(len(nums) + 1)) - sum(nums)
        
