class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        DP = [float("inf") for _ in dungeon[0]]
        DP[-1] = 1
        
        for i in reversed(xrange(len(dungeon))):
            DP[-1] = max(DP[-1] - dungeon[i][-1], 1)
            for j in reversed(xrange(len(dungeon[i]) - 1)):
                min_HP_on_exit = min(DP[j], DP[j + 1])
                DP[j] = max(min_HP_on_exit - dungeon[i][j], 1)
                
        return DP[0]
