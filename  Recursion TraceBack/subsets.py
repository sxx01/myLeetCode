from typing import List


class Solution:
    def traceback(self, i: int, n: int, nums: List[int]):
        if i == n:
            self.ans.append(self.str[:])
        else:
            self.str.append(nums[i])
            self.traceback(i + 1, n, nums)
            self.str.pop()
            self.traceback(i + 1, n, nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        self.str = []
        self.ans = []
        n = len(nums)
        self.traceback(0, n, nums)
        return self.ans


if __name__ == "__main__":
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    so = Solution()
    print(so.subsets(nums))
