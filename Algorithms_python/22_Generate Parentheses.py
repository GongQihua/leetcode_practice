class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(left, right, t):
            if left == n and right == n:
                ans.append(t)
                return
            if left < n:
                dfs(left+1, right, t+'(')
            if right < left:
                dfs(left, right+1, t+')')
        dfs(0,0,'')
        return ans
'''
深度优先搜索算法dfs，先添加左括号，然后扩展右括号，自动循环
'''