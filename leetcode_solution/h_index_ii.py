class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) / 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1

        return n - left
    
class Solution2(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # f(A)=10, f(B)=8, f(C)=5, f(D)=4, f(E)=3　→ h-index=4
        # f(A)=25, f(B)=8, f(C)=5, f(D)=3, f(E)=3　→ h-index=3
        lo, hi = 0, len(citations)
        while lo < hi:
            mid = (lo + hi) // 2
            if citations[mid] < len(citations) - mid:
                lo = mid + 1
            else:
                hi = mid
                
        return len(citations) - lo
