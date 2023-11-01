class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        a = abs(x)
        
        while(a != 0):
            temp = a % 10
            num = num * 10 + temp
            a = int(a/10)
            
        if x >= 0 and x==num:
            return True
        else:
            return False
        
'''
不能用字符串反转的情况下，直接反转数字最方便，去掉符号，反转数字。
'''