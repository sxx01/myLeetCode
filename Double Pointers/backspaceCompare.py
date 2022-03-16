class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        while i >= 0 and j >= 0:
            inum = 0
            while i >= 0:
                if s[i] == '#':
                    inum += 1
                    i -= 1
                elif inum > 0:
                    inum -= 1
                    i -= 1
                else:
                    break
            jnum = 0
            while j >= 0:
                if t[j] == '#':
                    jnum += 1
                    j -= 1
                elif jnum > 0:
                    jnum -= 1
                    j -= 1
                else:
                    break
            if i < 0 and j < 0:
                return True
            elif i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    s = input()
    t = input()
    so = Solution()
    print(so.backspaceCompare(s, t))
