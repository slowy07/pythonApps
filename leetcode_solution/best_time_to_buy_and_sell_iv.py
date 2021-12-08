class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        K = k + 1
        n = len(prices)

        if k >= n // 2:
            maxProf = 0
            buy = prices[0]
            for i in range(1, n):
                maxProf += max(0, prices[i] - prices[i - 1])
            return maxProf

        dp = [[0] * n for _ in range(K)]

        for i in range(1, K):
            buy = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j], prices[j] + buy, dp[i][j - 1])
                buy = max(buy, -prices[j] + dp[i - 1][j - 1])
        return dp[-1][-1]
