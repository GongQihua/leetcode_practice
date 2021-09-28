class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mi = prices[0]
        for i in prices[1:]:
            res = max(res, i - mi)
            mi = min(mi, i)
        return res
'''
mi用来找队列最小数，res找最大差，因为是顺序查找，不会存在反着减的问题
'''