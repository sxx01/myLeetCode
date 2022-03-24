from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1 or nums[0] >= len(nums) - 1:
            return True
        m = nums[0]
        i = 1
        while i <= m:
            m = max(m, nums[i] + i)
            if m >= len(nums) - 1:
                return True
            i += 1
        return False


if __name__ == "__main__":
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    print(Solution().canJump(nums))
