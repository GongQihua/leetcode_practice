class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        y = self.myPow(x, n >> 1)
        return y * y if (n & 1) == 0 else y * y * x
'''
模拟次方的过程，就n*n*n一层层往下乘
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def qpow(a: float, n: int) -> float:
            ans = 1
            while n:
                if n & 1:
                    ans *= a
                a *= a
                n >>= 1
            return ans
        return qpow(x,n) if n >= 0 else 1 / qpow(x, -n)
'''
还可以用快速幂的方法，将幂指数n拆分为若干个二进制位上的1的和，然后将x的n次幂转化为x的若干个幂的乘积。
'''