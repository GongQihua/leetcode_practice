class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
        sign = -1 if dividend * divisor < 0 else 1
        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        while a >= b:
            cnt = 0
            while a >= (b << (cnt + 1)):
                cnt += 1
            ans += 1 << cnt
            a -= b << cnt
            print('ans =',ans)            
        return sign * ans if INT_MIN <= sign * ans <= INT_MAX else INT_MAX
'''
除法本质上就是减法，相当于a>b时，每次减掉b，最后次数乘以符号
但是一次循环只能做一次减法，效率太低会导致超时，所以再加上快速幂的思想优化即可
'''