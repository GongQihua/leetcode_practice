class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        #print(words)
        return ' '.join(words[:: -1])

'''
把字符串去掉空格，达成列表，然后反向输出
这是第一步操作后得到的output：['the', 'sky', 'is', 'blue']
'''