class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if ns > nt:
            return self.isOneEditDistance(t, s)
        if nt - ns > 1:
            return False
        
        for i in range(ns):
                if s[i] != t[i]:
                    if ns == nt:
                        return s[i + 1:] == t[i + 1:]
                    else:
                        return s[i:] == t[i + 1:]
        
        return ns + 1 == nt

'''
很简单的思路，看了肯定会，就是先确定大小，用小的跟大的比，遇到不一样后，接下来的位数和大的位数一样
就符合题目了
'''