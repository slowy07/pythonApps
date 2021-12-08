class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        start = 0
        while count < len(nums):
            curr = start
            prev = nums[curr]
            while True:
                idx = (curr + k) % len(nums)
                nums[idx], prev = prev, nums[idx]
                curr = idx
                count += 1
                if start == curr:
                    break
            start += 1

        # sol 2
        # while k > 0:
        #     nums.insert(0, nums.pop())
        #     k -= 1

        # sol 3
        # nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
