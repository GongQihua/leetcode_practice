class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(list(s)))
            chars[k].append(s)
        return list(chars.values())
'''
如题，做法是哈希表的思路，建立一个字典，将不同字符串组合sorted重排列后，作为字典的key
然后将不同的排列形式存入key下，最后返回字典的value
'''