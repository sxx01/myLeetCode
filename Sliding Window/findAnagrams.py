from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
        if s_len < p_len:
            return []
        ans = []
        count = [0] * 26
        for i in range(p_len):
            count[ord(p[i]) - 97] += 1
            count[ord(s[i]) - 97] -= 1
        diff = 0
        for i in range(len(count)):
            if count[i] != 0:
                diff += 1
        if diff == 0:
            ans.append(0)
        for i in range(s_len - p_len):
            if count[ord(s[i]) - 97] == -1:
                diff -= 1
            elif count[ord(s[i]) - 97] == 0:
                diff += 1
            count[ord(s[i]) - 97] += 1
            if count[ord(s[i + p_len]) - 97] == 1:
                diff -= 1
            elif count[ord(s[i + p_len]) - 97] == 0:
                diff += 1
            count[ord(s[i + p_len]) - 97] -= 1
            if diff == 0:
                ans.append(i + 1)
        return ans


if __name__ == "__main__":
    s, p = input(), input()
    so = Solution()
    print(so.findAnagrams(s, p))
