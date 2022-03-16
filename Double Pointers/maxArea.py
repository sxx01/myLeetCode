from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        ans = 0
        while i < j:
            if min(height[i], height[j]) * (j - i) > ans:
                ans = min(height[i], height[j]) * (j - i)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans


if __name__ == "__main__":
    m = int(input())
    height = []
    for i in range(m):
        height.append(int(input()))
    so = Solution()
    print(so.maxArea(height))
