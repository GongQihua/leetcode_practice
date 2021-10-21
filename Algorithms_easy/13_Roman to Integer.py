class Solution:
    def romanToInt(self, s: str) -> int:
        
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        
        for i in range(len(s)):
            if i > 0 and dict[s[i]] > dict[s[i-1]]:
                result += dict[s[i]] - 2*dict[s[i-1]]
            else:
                result += dict[s[i]]
        return result