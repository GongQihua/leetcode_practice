class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorts = []
        res = []
        for n in reversed(nums):
            idx = bisect.bisect_left(sorts, n)
            res.append(idx)
            sorts.insert(idx, n)
        return res[::-1]