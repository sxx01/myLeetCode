from typing import List


class Solution:

    def dfs(self, i: int, j: int, m: int, n: int, grid: List[List[str]]):
        if i < 0 or j < 0 or i >= m or j >= n or self.vis[i][j] or grid[i][j] == '0':
            return
        direc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.vis[i][j] = True
        for d in direc:
            self.dfs(i + d[0], j + d[1], m, n, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        self.vis = []
        for i in range(m):
            self.vis.append([False] * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not self.vis[i][j]:
                    ans += 1
                    self.dfs(i, j, m, n, grid)
        return ans


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    grid = []
    for i in range(m):
        t = []
        for j in range(n):
            t.append(input())
        grid.append(t)
    so = Solution()
    print(so.numIslands(grid))
