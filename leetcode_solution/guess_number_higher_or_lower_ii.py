class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for _ in xrange(n + 1)]
        for j in xrange(n + 1):
            for i in reversed(xrange(j - 1)):
                dp[i][j] = min((k + 1) + max(dp[i][k], dp[k + 1][j]) for k in xrange(i, j))
        return dp[0][n]
