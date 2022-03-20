from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n <= 1:
            return 1
        if grid[0][0] == 1:
            return -1
        vis = []
        for i in range(n):
            vis.append([False]*n)
        q = deque()
        q.append((0, 0))
        ans = 1
        while len(q) != 0:
            tmp_q = deque()
            while len(q) != 0:
                tmp = q.popleft()
                if tmp == (n-1, n-1):
                    return ans
                for direc in [[-1, 0], [1, 0], [0, -1], [0, 1], [1, -1], [1, 1], [-1, -1], [-1, 1]]:
                    newi = tmp[0] + direc[0]
                    newj = tmp[1] + direc[1]
                    if newi < 0 or newj < 0 or newi >= n or newj >= n or grid[newi][newj] == 1 or vis[newi][newj]:
                        continue
                    vis[newi][newj] = True
                    tmp_q.append((newi, newj))
            ans += 1
            while len(tmp_q) != 0:
                q.append(tmp_q.popleft())
        return -1


if __name__ == "__main__":
    n = int(input())
    grid = []
    for i in range(n):
        t = []
        for j in range(n):
            t.append(int(input()))
        grid.append(t)
    so = Solution()
    print(so.shortestPathBinaryMatrix(grid))
