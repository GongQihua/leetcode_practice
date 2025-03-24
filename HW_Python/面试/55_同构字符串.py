'''
给定两个字符串 s 和 t ，判断它们是否是同构的。
如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if (s[i] in d1 and d1[s[i]] != t[i]) or (t[i] in d2 and d2[t[i]] != s[i]):
                return False
            d1[s[i]] = t[i]
            d2[t[i]] = s[i]
        return True