class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a = (ax2 - ax1) * (ay2 - ay1)
        b = (bx2 - bx1) * (by2 - by1)
        width = min(bx2, ax2) - max(bx1, ax1)
        height = min(ay2, by2) - max(ay1, by1)
        return a + b - max(height, 0) * max(width, 0)

'''
a面积加b面积减掉重叠面积，这种mid题可以多来一点
'''