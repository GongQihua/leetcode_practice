'''
给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为 更加简洁的规范路径。
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        names = path.split('/')
        stack = list()
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != '.':
                stack.append(name)
        return '/' + '/'.join(stack)