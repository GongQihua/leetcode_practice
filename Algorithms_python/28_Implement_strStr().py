class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1
'''
以字符串 haystack 的每一个字符为起点与字符串 needle 进行比较，若发现能够匹配的索引，直接返回即可。
'''