class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            t = prices[i] - prices[i - 1]
            res += max(t, 0)
        return res

'''
思路是贪心算法，只要把两天交易内上涨的部分全加起来就行了，等于赚最多
'''