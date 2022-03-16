from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif firstList[i][0] > secondList[j][1]:
                j += 1
            else:
                ans.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                else:
                    j += 1
        return ans


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    firstList = []
    secondList = []
    for i in range(m):
        firstList.append([int(input()), int(input())])
    for i in range(n):
        secondList.append([int(input()), int(input())])
    so = Solution()
    print(so.intervalIntersection(firstList, secondList))
