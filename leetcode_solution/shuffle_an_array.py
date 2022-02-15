import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.__nums = nums
        
        

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.__nums
        

    def shuffle(self):
        """
        :rtype: List[int]
        """
        nums = list(self.__nums)
        for i in xrange(len(nums)):
            j = random.randint(i, len(nums) - 1)
            nums[i], nums[j] = nums[j], nums[i]
            
        return nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
