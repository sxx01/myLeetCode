class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i - j] * j, dp[i], (i - j) * j)
        return dp[n]


if __name__ == "__main__":
    print(Solution().integerBreak(int(input())))
