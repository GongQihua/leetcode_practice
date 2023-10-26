class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans

'''
其实是数学题，5的几次方，就有几个0
'''