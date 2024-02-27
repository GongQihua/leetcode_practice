class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n
        stk = []
        for i, h in enumerate(heights):
            while stk and heights[stk[-1]] >= h:
                right[stk[-1]] = i
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        return max(h * (right[i] - left[i] - 1) for i, h in enumerate(heights))
'''
我们可以枚举每根柱子的高度 h 作为矩形的高度，利用单调栈，向左右两边找第一个高度小于 h 的下标 left_i, right_i。

那么此时矩形面积为 h \times (right_i-left_i-1)，求最大值即可。

时间复杂度 O(n)，空间复杂度 O(n)。其中 n 表示 heights 的长度。

单调栈模版：
stk = []
for i in range(n):
    while stk and check(stk[-1], i):
        stk.pop()
    stk.append(i)
'''