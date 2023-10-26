class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num - 1) % 9 + 1
'''       
可以看到，数根 9 个为一组，循环出现。我们可以得出下面的规律：
n = 0：数根是 0
n 是 9 的倍数：数根是 9
n 不是 9 的倍数：数根是 n % 9
将上面的规律用式子：(n - 1) % 9 + 1 统一表达。
'''