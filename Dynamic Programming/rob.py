from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums) - 1):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
        ans = dp[-1]
        dp = [0, nums[1], max(nums[1], nums[2])]
        for i in range(3, len(nums)):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))
        ans = max(ans, dp[-1])
        return ans


if __name__ == "__main__":
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    print(Solution().rob(nums))
