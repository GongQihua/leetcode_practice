class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True
'''
同时从前往后和从后往前检查，比较两数
记得跳过符号和把大写变小写
python检查是否为字母：[].isalnum()
变小写[].lower()
'''