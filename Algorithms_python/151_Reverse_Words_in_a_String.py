class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        i, n = 0, len(s)
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            if i < n:
                j = i
                while j < n and s[j] != ' ':
                    j += 1
                ans.append(s[i:j])
                i = j
        return ' '.join(ans[::-1])

'''
把字符串去掉空格，达成列表，然后反向输出
这是第一步操作后得到的output：['the', 'sky', 'is', 'blue']
'''