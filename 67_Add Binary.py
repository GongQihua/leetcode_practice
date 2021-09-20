class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2) #二进制转十进制
        y = int(b, 2)
        return bin(x + y)[2:] #十进制转二进制，但转完是0b10... 所以从第三位开始输出