class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def dfs(t):
            if len(t) == len(s):
                ans.append(t)
                return
            for c, v in cnt.items():
                if v > 1:
                    cnt[c] -= 2
                    dfs(c + t + c)
                    cnt[c] += 2
                    
        cnt = Counter(s)
        mid = ''
        for c, v in cnt.items():
            if v & 1:
                if mid:
                    return []
                mid = c
                cnt[c] -= 1
        ans = []
        dfs(mid)
        return ans
'''
回文排列需要满足至多有一个字符出现奇数次数。若不满足条件，答案提前返回。
找到出现奇数次的字符，作为中间字符（可以为空），分别向两边扩展，构造回文串。若串的长度与原串长度相等，将该串添加到答案中。
'''