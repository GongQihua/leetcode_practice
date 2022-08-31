class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(v % 2 for v in Counter(s).values()) <= 1
'''
要记住用python里的Counter这个函数，思路就是数奇数个数的数，不能超过一个
'''