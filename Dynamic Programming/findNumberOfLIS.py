from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * n
        cnt = [1] * n
        maxLen = 0
        ans = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and f[j] + 1 > f[i]:
                    f[i] = f[j] + 1
                    cnt[i] = cnt[j]
                elif nums[j] < nums[i] and f[j] + 1 == f[i]:
                    cnt[i] += cnt[j]
            if maxLen < f[i]:
                maxLen = f[i]
                ans = cnt[i]
            elif maxLen == f[i]:
                ans += cnt[i]
        return ans


if __name__ == "__main__":
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    print(Solution().findNumberOfLIS(nums))
