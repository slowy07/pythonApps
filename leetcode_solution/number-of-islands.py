import collections


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(grid, i, j):
            if grid[i][j] == "0":
                return False
            grid[i][j] = "0"
            q = collections.deque([(i, j)])
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == "1"
                    ):
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr, nc))
            return True

        count = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if bfs(grid, i, j):
                    count += 1
        return count
