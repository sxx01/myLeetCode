from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            m = i + nums[i]
            for j in range(i + 1, m + 1):
                if j >= len(nums):
                    break
                if dp[j] == -1 or dp[j] > dp[i] + 1:
                    dp[j] = dp[i] + 1
        return dp[-1]


if __name__ == "__main__":
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    print(Solution().jump(nums))
