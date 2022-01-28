class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i, n in enumerate(nums):
            if i > mx:
                return False
            mx = max(mx, i + n)
        return True
'''
贪心算法，思路很简单，首先任何一格都是可以必定到达的，一步步走就完了，除非遇到0
这样问题就能转变成，第几格加上这格能走几步，有没有这样一格能到末尾，贪心找最优解
'''