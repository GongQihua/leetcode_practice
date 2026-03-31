class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)

        leftmax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftmax[i] = max(leftmax[i - 1], height[i])
        
        rightmax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightmax[i] = max(rightmax[i + 1], height[i])

        ans = sum(min(rightmax[i], leftmax[i]) - height[i] for i in range(n))
        return ans