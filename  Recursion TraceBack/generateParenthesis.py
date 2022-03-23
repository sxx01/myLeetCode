from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        ans = []

        def traceback(left: int, right: int, temp: str):
            if left == n and right == n:
                ans.append(temp[:])
            if left < n:
                temp += '('
                left += 1
                traceback(left, right, temp)
                left -= 1
                temp = temp[:len(temp) - 1]
            if right < left:
                temp += ')'
                right += 1
                traceback(left, right, temp)
                right -= 1
                temp = temp[:len(temp) - 1]

        traceback(0, 0, "")
        return ans


if __name__ == "__main__":
    print(Solution().generateParenthesis(int(input())))
