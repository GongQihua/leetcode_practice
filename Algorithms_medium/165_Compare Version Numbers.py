class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j, m, n = 0, 0, len(version1), len(version2)
        while i < m or j < n:
            a = b = 0
            while i < m and version1[i] != '.':
                a = a * 10 + int(version1[i])
                i += 1
            while j < n and version2[j] != '.':
                b = b * 10 + int(version2[j])
                j += 1
            if a != b:
                return -1 if a < b else 1
            i += 1
            j += 1
        return 0

'''
思路就是把两个版本号，去掉中间的点，变成一个树，然后比大小，直接遍历去点即可
'''