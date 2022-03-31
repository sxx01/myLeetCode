class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right = right & (right - 1)
        return right


if __name__ == "__main__":
    print(Solution().rangeBitwiseAnd(int(input()), int(input())))
