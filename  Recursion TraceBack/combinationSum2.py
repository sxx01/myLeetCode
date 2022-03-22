from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        str = []
        candidates.sort()

        def traceback(index: int):
            if sum(str) == target:
                ans.append(str[:])
            while index < len(candidates):
                if sum(str) + candidates[index] > target:
                    return
                str.append(candidates[index])
                index += 1
                traceback(index)
                str.pop()
                while index < len(candidates) and candidates[index - 1] == candidates[index]:
                    index += 1

        traceback(0)
        return ans


if __name__ == "__main__":
    m = int(input())
    candidates = []
    for i in range(m):
        candidates.append(int(input()))
    target = int(input())
    print(Solution().combinationSum2(candidates, target))
