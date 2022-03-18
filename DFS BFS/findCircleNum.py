from typing import List
import collections


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.vis = [False] * n
        ans = 0
        q = collections.deque()
        for i in range(n):
            if not self.vis[i]:
                ans += 1
                q.append(i)
                while len(q) != 0:
                    t = q.popleft()
                    for index, connect in enumerate(isConnected[t]):
                        if connect == 1 and not self.vis[index]:
                            self.vis[index] = True
                            q.append(index)
        return ans


if __name__ == "__main__":
    m = int(input())
    isConnected: List[List[int]] = []
    for i in range(m):
        t = []
        for j in range(m):
            t.append(int(input()))
        isConnected.append(t)
    so = Solution()
    print(so.findCircleNum(isConnected))
