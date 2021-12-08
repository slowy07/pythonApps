class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 1

        @lru_cache(maxsize=None)
        def go(i):
            n = nums[i]

            return 1 + max((go(j) for j in range(i + 1, l) if nums[j] > n), default=0)

        return max(go(i) for i in range(l))
