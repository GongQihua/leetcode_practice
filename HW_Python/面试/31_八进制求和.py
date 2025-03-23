class Solution:
    def addOctal(self, a: str, b: str) -> str:
        ans = []  # 使用列表存储结果
        carry = 0  # 进位标志
        n = max(len(a), len(b))  # 获取较长的字符串长度

        for i in range(n):
            # 从末尾开始逐位相加
            if i < len(a):
                carry += ord(a[-(i + 1)]) - ord('0')  # 使用 ord() 转换为整数
            if i < len(b):
                carry += ord(b[-(i + 1)]) - ord('0')  # 使用 ord() 转换为整数
            ans.append(str(carry % 8))  # 当前位的结果
            carry //= 8  # 计算进位

        if carry > 0:
            ans.append(str(carry))  # 处理最高位的进位

        ans.reverse()  # 反转结果
        return ''.join(ans)  # 将列表转换为字符串并返回