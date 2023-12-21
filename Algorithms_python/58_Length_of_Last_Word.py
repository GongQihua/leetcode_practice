class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        j = i
        while j >= 0 and s[j] != ' ':
            j -= 1
        return i - j
'''
我们从字符串s末尾开始遍历，找到第一个不为空格的字符，即为最后一个单词的最后一个字符，下标记为i。
然后继续向前遍历，找到第一个为空格的字符，即为最后一个单词的第一个字符的前一个字符，记为j。
那么最后一个单词的长度即为i - j。
'''