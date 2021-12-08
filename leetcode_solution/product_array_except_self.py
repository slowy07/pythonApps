class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m, res = 1, []
        for i in range(len(nums)):
            res.append(m)
            m *= nums[i]

        m = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= m
            m *= nums[i]

        return res
