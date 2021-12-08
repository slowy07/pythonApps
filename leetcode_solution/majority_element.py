import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return collections.Counter(nums).most_common(1)[0][0]
