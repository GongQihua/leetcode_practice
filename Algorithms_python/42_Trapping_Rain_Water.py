class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        leftmax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], height[i])
        rightmax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n-2, -1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i])
        ans = sum(min(leftmax[i], rightmax[i]) - height[i] for i in range(n))
        return ans
    
    def trap2(self, height: List[int]) -> int: # 基于上一种方法的优化，双指针一遍遍历，思路是一样的
        ans = 0
        left, right = 0, len(height) - 1
        leftmax = rightmax = 0

        while left < right:
            leftmax = max(leftmax, height[left])
            rightmax = max(rightmax, height[right])
            if height[left] < height[right]:
                ans += leftmax - height[left]
                left += 1
            else:
                ans += rightmax - height[right]
                right -= 1
                
        return ans
'''
正向遍历找leftmax的每一个值，再反向遍历找rightmax的每一个值，
然后用小的那个值减现有值，再累加得到解。
'''