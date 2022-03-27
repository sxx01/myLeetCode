from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and wordDict.count(s[j:i]) != 0:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    s = input()
    n = int(input())
    wordDict = []
    for _ in range(n):
        wordDict.append(input())
    print(Solution().wordBreak(s, wordDict))
