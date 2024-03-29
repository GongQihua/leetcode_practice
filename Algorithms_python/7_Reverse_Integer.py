class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        a = abs(x) #去符号
        
        while(a != 0):
            temp = a % 10
            num = num * 10 + temp
            a = int(a/10)
            
        if x > 0 and num < 2147483647: #2**31，最大32位
            return num
        elif x < 0 and num <= 2147483647:
            return -num
        else:
            return 0
        
'''
easy题，直接做成字符串反转也行
'''