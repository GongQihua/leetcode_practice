class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i -j - 1]
        return dp[-1]
'''
思路：假设 n 个节点存在二叉搜索树的个数是 G(n)，1 为根节点，2 为根节点，...，n 为根节点，
当 1 为根节点时，其左子树节点个数为 0，右子树节点个数为 n-1，
同理当 2 为根节点时，其左子树节点个数为 1，右子树节点为 n-2，
所以可得 G(n) = G(0) * G(n-1) + G(1) * (n-2) + ... + G(n-1) * G(0)。
'''