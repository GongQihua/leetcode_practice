'''
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        f = [True] + [False] * n
        for i in range(1, n + 1):
            for j in range(i):
                if f[j] and (s[j:i] in wordDict):
                    f[i] = True
                    break
        return f[-1]