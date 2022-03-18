from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        mul = 1
        for right, val in enumerate(nums):
            mul *= val
            while left <= right:
                if mul < k:
                    ans += (right - left + 1)
                    break
                mul /= nums[left]
                left += 1
        return ans


if __name__ == "__main__":
    m = int(input())
    nums = []
    for i in range(m):
        nums.append(int(input()))
    k = int(input())
    so = Solution()
    print(so.numSubarrayProductLessThanK(nums, k))
