from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        vis = []
        for i in range(m):
            vis.append([False] * n)

        def dfs(i: int, j: int, idx: int):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= m or j >= n or vis[i][j] or board[i][j] != word[idx]:
                return False
            vis[i][j] = True
            idx += 1
            ans = dfs(i + 1, j, idx) or dfs(i - 1, j, idx) or dfs(i, j + 1, idx) or dfs(i, j - 1, idx)
            vis[i][j] = False
            return ans

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    vis = []
                    for _ in range(m):
                        vis.append([False] * n)
                    if dfs(i, j, 0):
                        return True
        return False


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    board = []
    for i in range(m):
        t = []
        for j in range(n):
            t.append(input())
        board.append(t)
    word = input()
    print(Solution().exist(board, word))
