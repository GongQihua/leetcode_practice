class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda b: b[1])
        pos = points[0][1]
        ans = 1
        for ballon in points:
            if ballon[0] > pos:
                ans += 1
                pos = ballon[1]
        return ans