from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        if n <= 2 or nums[0] > 0 or nums[n - 1] < 0:
            return []
        ans = []
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            tmp = -nums[i]
            j, k = i + 1, n - 1
            while j < n and k < n and j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                if nums[j] + nums[k] == tmp:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] <= tmp:
                    j += 1
                else:
                    k -= 1
        return ans


if __name__ == "__main__":
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    so = Solution()
    print(so.threeSum(nums))
