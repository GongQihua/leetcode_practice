class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(" : ")", "{" : "}", "[" : "]"}
        
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