import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        lookup = collections.defaultdict(int)
        for i in nums1:
            lookup[i]  += 1
        
        res = []
        for i in nums2:
            if lookup[i] > 0:
                res += i,
                lookup[i] -= 1
        
        return res
      
