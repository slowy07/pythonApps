from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [i for i, j in Counter(nums).items() if j > len(nums) // 3]
