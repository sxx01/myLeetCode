from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and f[j] + 1 > f[i]:
                    f[i] = f[j] + 1
        return max(f)


if __name__ == "__main__":
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    print(Solution().lengthOfLIS(nums))
