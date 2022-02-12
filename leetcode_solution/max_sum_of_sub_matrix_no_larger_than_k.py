from bisect import bisect_left, insort

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
        
        m = min(len(matrix), len(matrix[0]))
        n = max(len(matrix), len(matrix[0]))
        result = float("-inf")
        
        for i in xrange(m):
            sums = [0] * n
            for j in xrange(i, m):
                for l in xrange(n):
                    sums[l] += matrix[j][l] if m == len(matrix) else matrix[l][j]
                
                accu_sum_set, accu_sum = [0], 0
                for sum in sums:
                    accu_sum += sum
                    it = bisect_left(accu_sum_set, accu_sum - k)
                    if it != len(accu_sum_set):
                        result = max(result, accu_sum - accu_sum_set[it])
                    insort(accu_sum_set, accu_sum)
        return result
        
