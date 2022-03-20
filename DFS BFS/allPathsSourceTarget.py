from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        str = list()
        ans = list()
        n = len(graph)

        def dfs(i: int):
            if i == n - 1:
                ans.append(str[:])
            else:
                for j in graph[i]:
                    str.append(j)
                    dfs(j)
                    str.pop()

        str.append(0)
        dfs(0)
        return ans
