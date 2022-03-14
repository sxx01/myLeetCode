from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]


if __name__ == "__main__":
    m: int = int(input())
    nums: List[int] = []
    for i in range(m):
        t: int = int(input())
        nums.append(t)
    so = Solution()
    ans: int = so.findMin(nums)
    print(ans)
