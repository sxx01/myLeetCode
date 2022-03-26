from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        n = len(nums)
        dp = []
        for i in range(n):
            dp.append([False] * n)
        for i in range(n - 2):
            if nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1]:
                dp[i][i + 2] = True
        for i in range(3, n):
            for j in range(n - i):
                l = j
                r = j + i
                if dp[l][r - 1] and nums[r - 1] - nums[r - 2] == nums[r] - nums[r - 1]:
                    dp[l][r] = True
        ans = 0
        for i in range(n):
            for j in range(i + 2, n):
                if dp[i][j]:
                    ans += 1
        return ans


if __name__ == "__main__":
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    print(Solution().numberOfArithmeticSlices(nums))
