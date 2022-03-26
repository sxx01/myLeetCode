class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        n = len(s)
        dp = []
        for _ in range(n):
            dp.append([False] * n)
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
        for i in range(2, n):
            for j in range(n - i):
                l = j
                r = j + i
                if dp[l + 1][r - 1] and s[l] == s[r]:
                    dp[l][r] = True
        ans = ""
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] and (j - i + 1 > len(ans)):
                    ans = s[i:j + 1]
        return ans


if __name__ == "__main__":
    print(Solution().longestPalindrome(input()))
