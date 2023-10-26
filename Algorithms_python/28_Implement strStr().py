class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1): #截取needle长度遍历数组
            if haystack[i: i+len(needle)] == needle: #检验截取part是否与needle相符
                return i
        return -1