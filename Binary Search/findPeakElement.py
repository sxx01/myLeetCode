from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        def get(i: int):
            if i < 0 or i >= n:
                return -float('inf')
            return nums[i]

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if get(m - 1) < get(m) > get(m + 1):
                return m
            if get(m) < get(m + 1):
                l = m + 1
            else:
                r = m - 1


if __name__ == "__main__":
    m = int(input())
    nums = []
    for i in range(m):
        nums.append(int(input()))
    so = Solution()
    print(so.findPeakElement(nums))
