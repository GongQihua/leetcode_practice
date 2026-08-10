class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = 0
        t_sum = 0
        for ch in s:
            s_sum += ord(ch)
        for ch in t:
            t_sum += ord(ch)
        return chr(t_sum - s_sum)