class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for a, b in zip(s, t):
            if a in d1 and d1[a] != b:
                return False
            if b in d2 and d2[b] != a:
                return False
            d1[a] = b
            d2[b] = a
        return True

'''
这个映射其实意思很怪，需要理解一下的，相当于结构相似
用哈希表来存储结构，这里用了个zip，可以打包几个数组变成元组
'''