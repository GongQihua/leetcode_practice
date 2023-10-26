class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n
        while left < right:
            mid = (left + right + 1) >> 1
            if citations[n - mid] >= mid:
                left = mid
            else:
                right = mid - 1
        return left
'''
二分枚举 h，获取满足条件的最大 h。由于要满足 h 篇论文至少被引用 h 次，因此 citations[n - mid] >= mid。
时间复杂度 O(logn)。
'''