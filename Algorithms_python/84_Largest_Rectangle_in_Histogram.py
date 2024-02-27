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

这里涉及到数据结构单调栈，构造思路：

栈中存放了 j 值。从栈底到栈顶，j 的值严格单调递增，同时对应的高度值也严格单调递增；

当我们枚举到第 i 根柱子时，我们从栈顶不断地移除 height[j]≥height[i] 的 j 值。在移除完毕后，栈顶的 j 值就一定满足 height[j]<height[i]，此时 j 就是 i 左侧且最近的小于其高度的柱子。

这里会有一种特殊情况。如果我们移除了栈中所有的 j 值，那就说明 i 左侧所有柱子的高度都大于 height[i]，那么我们可以认为 i 左侧且最近的小于其高度的柱子在位置 j=−1，它是一根「虚拟」的、高度无限低的柱子。这样的定义不会对我们的答案产生任何的影响，我们也称这根「虚拟」的柱子为「哨兵」。
我们再将 i 放入栈顶。

栈中存放的元素具有单调性，这就是经典的数据结构「单调栈」了。

'''