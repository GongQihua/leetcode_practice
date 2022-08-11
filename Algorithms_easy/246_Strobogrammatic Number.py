class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        def match(a, b):
            if a in {'0', '1', '8'}:
                return a == b
            if a == '6':
                return b == '9'
            if a == '9':
                return b == '6'
            return False
        
        n = len(num)
        i, j = 0, n - 1
        while i <= j:
            if not match(num[i], num[j]):
                return False
            i += 1
            j -= 1
        return True
'''
能中心旋转的数字就那几个，所以思路就是，导入数组前后对应数，然后分情况讨论就行
比如0，1，8怎么都是一样的，但6，9要对位旋转。
'''