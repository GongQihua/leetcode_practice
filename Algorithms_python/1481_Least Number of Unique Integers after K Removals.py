class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        t = sorted(counter.items(), key=lambda x: x[1])
        for v, cnt in t:
            if k >= cnt:
                k -= cnt
                counter.pop(v)
            else:
                break
        return len(counter)
'''
思路就是从小到大排出数组和个数，然后优先杀掉一种变化
'''