from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        map = {}
        ans = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if points[j][0] - points[i][0] == 0:
                    tan = float('inf')
                    bias = float('inf')
                else:
                    tan = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    bias = points[i][1] - tan * points[i][0]

                # print("=" * 5)
                # print(i, j)
                # print(points[i][0], points[i][1])
                # print(points[j][0], points[j][1])
                # print(tan)
                # print("=" * 5)

                if (tan, bias) not in map.keys():
                    map[(tan, bias)] = 1
                else:
                    continue
                tmpans = 2
                for k in range(len(points)):
                    if k != i and k != j:
                        if points[k][0] - points[i][0] == 0:
                            tmptan = float('inf')
                        else:
                            tmptan = (points[k][1] - points[i][1]) / (points[k][0] - points[i][0])
                        if tmptan == tan:
                            tmpans += 1
                if tmpans > ans:
                    ans = tmpans
        return ans


if __name__ == "__main__":
    n = int(input())
    points = []
    for _ in range(n):
        points.append([int(input()), int(input())])
    print(Solution().maxPoints(points))
