class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        def countAndMergeSort(sums, start, end, lower, upper):
            if end - start <= 1:
                return 0
            mid = start + (end - start) / 2
            count = countAndMergeSort(
                sums, start, mid, lower, upper
            ) + countAndMergeSort(sums, mid, end, lower, upper)

            j, k, r = mid, mid, mid
            tmp = []
            for i in xrange(start, mid):
                while k < end and sums[k] - sums[i] < lower:
                    k += 1
                while j < end and sums[j] - sums[i] <= upper:
                    j += 1

                count += j - k

                while r < end and sums[r] < sums[i]:
                    tmp.append(sums[r])
                    r += 1

                tmp.append(sums[i])

            sums[start : start + len(tmp)] = tmp
            return count

        sums = [0] * (len(nums) + 1)
        for i in xrange(len(nums)):
            sums[i + 1] = sums[i] + nums[i]
        return countAndMergeSort(sums, 0, len(sums), lower, upper)
    
    
#     class Solution2(object):
#     def countRangeSum(self, nums, lower, upper):
#         """
#         :type nums: List[int]
#         :type lower: int
#         :type upper: int
#         :rtype: int
#         """
#         first = [0]
#         for num in nums:
#             first.append(first[-1] + num)
        
#         def sort(lo, hi):
#             mid = (lo + hi) / 2
#             if mid == lo:
#                 return 0
#             count = sort(lo, mid) + sort(mid, hi)
#             i = j = mid
#             for left in first[lo:mid]:
#                 while i < hi and first[i] - left < lower:
#                     i += 1
#                 while j < hi and first[j] - left <= upper:
#                     j += 1
                
#                 count += j - i
#             first[lo:hi] = sorted(first[lo:hi]) 
#             return count
        
#         return sort(0, len(first))
