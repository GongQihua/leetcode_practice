class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        vis = {1}
        ans = 1
        for _ in range(n):
            ans = heappop(h)
            for v in [2, 3, 5]:
                nxt = ans * v
                if nxt not in vis:
                    vis.add(nxt)
                    heappush(h, nxt)
        return ans
'''
方法一：优先队列（最小堆）
初始时，将第一个丑数 1 加入堆。每次取出堆顶元素 x，由于 2x, 3x, 5x 也是丑数，因此将它们加入堆中。为了避免重复元素，可以用哈希表  去重。
时间复杂度 $O(nlogn)$，空间复杂度 $O(n)$。

方法二：动态规划

定义数组 $dp$，$dp[i-1]$ 表示第 $i$ 个丑数，那么第 $n$ 个丑数就是 $dp[n - 1]$。最小的丑数是 $1$，所以 $dp[0]=1$。
定义 $3$ 个指针 $p_2$，$p_3$，$p_5$，表示下一个丑数是当前指针指向的丑数乘以对应的质因数。初始时，三个指针的值都指向 $0$。
当 $i∈[1,n)$，$dp[i]=min(dp[p_2] \ * 2, dp[p_3] \ * 3, dp[p_5] \ * 5)$，然后分别比较 $dp[i]$ 与 $dp[p_2] \ * 2$、$dp[p_3] \ * 3$、$dp[p_5] \ * 5$ 是否相等，若是，则对应的指针加 $1$。
最后返回 $dp[n-1]$ 即可。
时间复杂度 $O(n)$，空间复杂度 $O(n)$。
'''