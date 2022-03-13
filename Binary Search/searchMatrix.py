from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        up = -1
        down = row - 1
        while up < down:
            mid = (down - up + 1) // 2 + up
            if matrix[mid][0] <= target:
                up = mid
            else:
                down = mid - 1
        left = 0
        right = col - 1
        mid = up
        while left <= right:
            m = (left + right) // 2
            if matrix[mid][m] == target:
                return True
            if matrix[mid][m] < target:
                left = m + 1
            else:
                right = m - 1
        return False


if __name__ == "__main__":
    m: int = int(input())
    n: int = int(input())
    matrix: List[List[int]] = []
    for i in range(m):
        t: List[int] = []
        for j in range(n):
            t.append(int(input()))
        matrix.append(t)
    target: int = int(input())
    so = Solution()
    ans: bool = so.searchMatrix(matrix, target)
    print(ans)
