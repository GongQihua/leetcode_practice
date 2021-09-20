class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        if x == 0:
            return 0
        while left < right:
            mid = (left + right + 1) // 2
            if x // mid >= mid:
                left = mid
            else:
                right = mid - 1
        return left
        #用找中位数的方法无限逼近平方根，用mid*mid <= x来判断，也就是第九行