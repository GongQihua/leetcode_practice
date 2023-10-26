class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        neg = (numerator > 0) ^ (denominator > 0)
        if neg:
            res.append('-')
        num, d = abs(numerator), abs(denominator)
        res.append(str(num // d))
        num %= d
        if num == 0:
            return ''.join(res)
        res.append('.')
        mp = {}
        while num != 0:
            mp[num] = len(res)
            num *= 10
            res.append(str(num // d))
            num %= d
            if num in mp:
                idx = mp[num]
                res.insert(idx, '(')
                res.append(')')
                break
        return ''.join(res)

'''
先判断正负，和是否一次能除尽，然后不断%=，如果要遇到无限循环的小数
在进行除法时使用 HashMap 存储余数及其关联的索引，这样每当出现相同的余数时，我们就知道有一个重复的小数部分。
'''