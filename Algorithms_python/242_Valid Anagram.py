class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = [0] * 26
        for i in range(len(s)):
            chars[ord(s[i]) - ord('a')] += 1
            chars[ord(t[i]) - ord('a')] -= 1
        return all(c == 0 for c in chars)

'''
数组或哈希表累加 s 中每个字符出现的次数，再减去 t 中对应的每个字符出现的次数。
遍历结束后，若字符中出现次数不为 0 的情况，返回 false，否则返回 true。
'''