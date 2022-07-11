class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s) - 10
        cnt = Counter()
        ans = []
        for i in range(n + 1):
            sub = s[i : i + 10]
            cnt[sub] += 1
            if cnt[sub] == 2:
                ans.append(sub)
        return ans

'''
标准的哈希表题目
使用哈希表，记录所有连续长度为 10 的子字符串出现次数（字符串为 Key，次数为 Value，
当出现一次以上时，将其加入返回列表当中。
'''