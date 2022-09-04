class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)
        for c in citations:
            if c <= n:
                cnt[c] += 1
            else:
                cnt[n] += 1
            #print('cnt = ',cnt)
        sum = 0
        for i in range(n, -1, -1):
            sum += cnt[i]
            if sum >= i:
                return i
        return 0
'''
最简单的解法就是排序之后再判断，但是因为 H 不可能大于论文的总数 n，所以可以用计数排序进行优化。
举个例子：
Your input
[3,0,6,1,5]
stdout
cnt =  [0, 0, 0, 1, 0, 0]
cnt =  [1, 0, 0, 1, 0, 0]
cnt =  [1, 0, 0, 1, 0, 1]
cnt =  [1, 1, 0, 1, 0, 1]
cnt =  [1, 1, 0, 1, 0, 2]
'''