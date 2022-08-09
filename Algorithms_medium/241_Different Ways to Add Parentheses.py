class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def dfs(exp):
            if exp.isdigit():
                return[int(exp)]
            ans = []
            for i, c in enumerate(exp):
                if c in '-+*':
                    left, right = dfs(exp[:i]), dfs(exp[i + 1:])
                    for a in left:
                        for b in right:
                            if c == '-':
                                ans.append(a - b)
                            if c == '+':
                                ans.append(a + b)
                            if c == '*':
                                ans.append(a * b)
            return ans
        return dfs(expression)
'''
记忆搜索法
'''