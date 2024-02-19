class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        for s in path.split('/'):
            if not s or s == '.':
                continue
            if s == '..':
                if ans:
                    ans.pop()
            else:
                ans.append(s)
        return '/' + '/'.join(ans)
'''
我们先将路径按照 '/' 分割成若干个子串，然后遍历每个子串，根据子串的内容进行如下操作：

若子串为空，或者为 '.'，则不做任何操作，因为 '.' 表示当前目录；
若子串为 '..'，则需要将栈顶元素弹出，因为 '..' 表示上一级目录；
若子串为其他字符串，则将该子串入栈，因为该子串表示当前目录的子目录。

最后，我们将栈中的所有元素按照从栈底到栈顶的顺序拼接成字符串，即为简化后的规范路径。
'''