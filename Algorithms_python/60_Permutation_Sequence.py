class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        vis = [False] * (n + 1)
        for i in range(n):
            fact = 1
            for j in range(1, n - i):
                fact *= j
            for j in range(1, n + 1):
                if not vis[j]:
                    if k > fact:
                        k -= fact
                    else:
                        ans.append(str(j))
                        vis[j] = True
                        break
        return ''.join(ans)
'''
集合[1,2,3.....n]  一共有n! 种排列，如果我们确定首位，那剩余位能组成的排列数量为(n-1)! 。

因此，我们枚举每一位i，如果此时 k大于当前位置确定后的排列数量，那么我们可以直接减去这个数量；

否则，说明我们找到了当前位置的数。

对于每一位i，其中0<=i<n ，剩余位能组成的排列数量为(n-i-1)!，我们记为fact。过程中已使用的数记录在 vis 中。
'''