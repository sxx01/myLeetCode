from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        map = [[], [], 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = []

        def traceback(idx: int, temp: str):
            if idx == len(digits):
                ans.append(temp[:])
                return
            letters = map[ord(digits[idx]) - ord('0')]
            for i in letters:
                temp += i
                traceback(idx + 1, temp)
                temp = temp[:len(temp) - 1]

        traceback(0, "")
        return ans


if __name__ == "__main__":
    print(Solution().letterCombinations(input()))
