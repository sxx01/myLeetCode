from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        str = []
        vis = [False] * len(nums)
        nums.sort()

        def traceBack():
            if len(str) == len(nums):
                ans.append(str[:])
            i = 0
            while i < len(nums):
                if vis[i]:
                    i += 1
                    continue
                vis[i] = True
                str.append(nums[i])
                traceBack()
                str.pop()
                vis[i] = False
                i += 1
                while i < len(nums) and nums[i - 1] == nums[i]:
                    i += 1

        traceBack()
        return ans


if __name__ == "__main__":
    m = int(input())
    nums = []
    for i in range(m):
        nums.append(int(input()))
    so = Solution()
    print(so.permuteUnique(nums))
