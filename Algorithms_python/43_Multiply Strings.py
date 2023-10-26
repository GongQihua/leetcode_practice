class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def add(s1, s2):
            x1, x2 = len(s1), len(s2)
            i = carry = 0
            res = []
            while i < max(x1, x2) or carry > 0:
                a = int(s1[x1 - i - 1]) if i < x1 else 0 
                b = int(s2[x2 - i - 1]) if i < x2 else 0 
                carry, t = divmod(a + b + carry, 10)
                res.append(str(t))
                i += 1
            return ''.join(res[::-1])
        
        if '0' in [num1, num2]:
            return '0'
        n1, n2 = len(num1), len(num2)
        ans = ''
        for i in range(n1):
            a = int(num1[n1 - i - 1])
            t = ''
            for j in range(n2):
                b = int(num2[n2 - j - 1])
                t = add(t, str(a*b) + '0' * j)
            ans = add(ans, t + '0' * i)
        return ans
'''
乘法运算的思路，两个数，没个数的每一位都要与另一个数的另一位相乘，所以基础是两个循环
第二点是数值运算和数组的相互转换，另写了一个def就是干这个用的，注意格式，注意位数
'''