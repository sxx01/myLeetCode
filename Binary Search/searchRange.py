from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int, lower: bool) -> int:
        l = 0
        r = len(nums) - 1
        ans = len(nums)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target or (lower and nums[mid] >= target):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftIdx = self.binarySearch(nums, target, True)
        rightIdx = self.binarySearch(nums, target, False) - 1
        if (leftIdx <= rightIdx and rightIdx < len(nums) and nums[leftIdx] == target and nums[rightIdx] == target):
            return [leftIdx, rightIdx]
        return [-1, -1]


if __name__ == "__main__":
    m: int = int(input())
    nums: List[int] = []
    for i in range(m):
        t: int = int(input())
        nums.append(t)
    target: int = int(input())
    so = Solution()
    ans: List[int] = so.searchRange(nums, target)
    print(ans)
