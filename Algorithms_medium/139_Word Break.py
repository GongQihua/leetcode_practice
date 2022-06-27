class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                #print(s[j : i])
                if dp[j] and s[j : i] in words:
                    dp[i] = True
                    break
        return dp[n]

'''
主要想法就是建一个列表遍历，差分字母成不同组合，看能不能和字典里的对上
dp[i] 表示前 i 个字符组成的字符串 s[0...i-1] 能否拆分成若干个字典中出现的单词。
'''