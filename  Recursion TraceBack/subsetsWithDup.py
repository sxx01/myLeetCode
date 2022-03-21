from typing import List


class Solution:
    def traceback(self, i: int, nums: List[int]):
        self.ans.append(self.str[:])
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            else:
                self.str.append(nums[j])
                self.traceback(j + 1, nums)
                self.str.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        nums.sort()
        self.str = []
        self.ans = []
        self.traceback(0, nums)
        return self.ans


if __name__ == "__main__":
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    so = Solution()
    print(so.subsetsWithDup(nums))
