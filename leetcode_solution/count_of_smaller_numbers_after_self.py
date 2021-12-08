class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def countAndMergeSort(num_idxs, start, end, counts):
            if end - start <= 0:
                return 0

            mid = start + (end - start) / 2
            countAndMergeSort(num_idxs, start, mid, counts)
            countAndMergeSort(num_idxs, mid + 1, end, counts)

            r = mid + 1
            tmp = []
            for i in xrange(start, mid + 1):
                while r <= end and num_idxs[r][0] < num_idxs[i][0]:
                    tmp.append(num_idxs[r])
                    r += 1
                tmp.append(num_idxs[i])
                counts[num_idxs[i][1]] += r - (mid + 1)

            num_idxs[start : start + len(tmp)] = tmp

        num_idxs = []
        counts = [0] * len(nums)
        for i, num in enumerate(nums):
            num_idxs.append((num, i))

        countAndMergeSort(num_idxs, 0, len(num_idxs) - 1, counts)
        return counts
