from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        str = []
        candidates.sort()

        def traceback(i: int):
            if sum(str) == target:
                ans.append(str[:])
            for j in range(i, len(candidates)):
                if sum(str) + candidates[j] > target:
                    continue
                str.append(candidates[j])
                traceback(i)
                str.pop()
                i += 1

        traceback(0)
        return ans


if __name__ == "__main__":
    m = int(input())
    candidates = []
    for i in range(m):
        candidates.append(int(input()))
    target = int(input())
    print(Solution().combinationSum(candidates, target))
