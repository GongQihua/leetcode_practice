class Solution:
    def isHappy(self, n: int) -> bool:
        def nextnum(n):
            s = 0
            while n > 0:
                n, nmod = divmod(n, 10)
                s += nmod ** 2
            return s
        visit = set()
        while n != 1 and n not in visit:
            visit.add(n)
            n = nextnum(n)
        return n == 1
'''
建立一个不重复的list，在不断更新n的过程中，判断是否该数已经出现
否则继续存入，知道停止
最后判断n是否等于1，返回true false
'''