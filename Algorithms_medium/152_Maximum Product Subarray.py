class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxf = minf = res = nums[0]
        for num in nums[1:]:
            m, n = maxf, minf
            maxf = max(num, m * num, n * num)
            minf = min(num, m * num, n * num)
            res = max(res, maxf)
        return res

'''
思考两种可能性，
如果是一个负数的话，那么我们希望以它前一个位置结尾的某个段的积也是个负数，这样可以负负得正，并且我们希望这个积尽可能「负得更多」，即尽可能小。
如果是一个正数的话，我们更希望以它前一个位置结尾的某个段的积也是个正数，并且希望它尽可能地大。
'''