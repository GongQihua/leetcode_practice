class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #创建一个删除式list
        mapping = {"(" : ")", "{" : "}", "[" : "]"} #对照表dict
        #思路：将前一半字符放入对照表，对应另一半字符，遇到前一半字符，则将对应
        #     的另一半存入空list中，遇后一半字符则检测list中前一位是否与它相同
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        if not stack:
            return True
        else:
            return False