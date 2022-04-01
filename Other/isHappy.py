class Solution:
    def isHappy(self, n: int) -> bool:
        used = {}
        while True:
            if n in used.keys():
                return False
            else:
                used[n] = 1
            tmp = 0
            while n > 0:
                tmp += (n % 10) ** 2
                n //= 10
            if tmp == 1:
                return True
            n = tmp


if __name__ == "__main__":
    print(Solution().isHappy(int(input())))
