from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        ans = 0
        sum = 0
        for right, val in enumerate(nums):
            sum += val
            while left <= right and sum >= target:
                if ans == 0 or (right - left + 1) < ans:
                    ans = right - left + 1
                sum -= nums[left]
                left += 1
        return ans


if __name__ == "__main__":
    target = int(input())
    m = int(input())
    nums = []
    for i in range(m):
        nums.append(int(input()))
    so = Solution()
    print(so.minSubArrayLen(target, nums))
