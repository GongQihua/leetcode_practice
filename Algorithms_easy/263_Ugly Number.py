class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        for x in [2, 3, 5]:
            while n % x == 0:
                n //= x
        return n == 1
'''
若 n < 1，说明 n 一定不是丑数，返回 false。
若 n % 2 == 0，说明 2 是 n 的因子，此时应 n /= 2，然后继续判断 n 除以 2 后的值的因子。
若 n % 3 == 0，说明 3 是 n 的因子，此时应 n /= 3，然后继续判断 n 除以 3 后的值的因子。
若 n % 5 == 0，说明 5 是 n 的因子，此时应 n /= 5，然后继续判断 n 除以 5 后的值的因子。
最后，判断 n 是否等于 1，若是，说明 n 的因子只可能包含 2、3、5，返回 true；否则返回 false。
'''