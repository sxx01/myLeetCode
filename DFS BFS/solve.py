from typing import List


class Solution:

    def dfs(self, i: int, j: int, m: int, n: int, board: List[List[str]]):
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] == 'X' or self.vis[i][j]:
            return
        self.vis[i][j] = True
        for direc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            self.dfs(i + direc[0], j + direc[1], m, n, board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        if m == 1 or n == 1:
            return
        self.vis = []
        for i in range(m):
            self.vis.append([False] * n)
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][j] == 'O' and not self.vis[i][j]:
                    self.dfs(i, j, m, n, board)
        for i in range(m):
            for j in range(n):
                if not self.vis[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    board = []
    for i in range(m):
        t = []
        for j in range(n):
            t.append(input())
        board.append(t)
    so = Solution()
    so.solve(board)
    for i in range(m):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
