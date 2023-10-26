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
其实思路就是挨个加入，遇到.跳过，将被/分割的字母一个个提出来，组成新字符串，在join加入/
'''