class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        return (
            (D - B) * (C - A)
            + (G - E) * (H - F)
            - max(0, (min(C, G) - max(A, E))) * max(0, (min(D, H) - max(B, F)))
        )
