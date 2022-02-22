class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort(key=lambda x: x[0])
            print(intervals)
            st = ed = -1
            res = []
            for s, e in intervals:
                if ed < s:
                    if st != -1:
                        res.append([st,ed])
                    st, ed = s, e
                else:
                    ed = max(ed, e)
            if st != -1:
                res.append([st, ed])
            return res
        
        intervals.append(newInterval)
        return merge(intervals)
'''
做法就是设定两个中立数，暴力搜索比较，然后迭代，以此来合并数集
方法实现的关键是排序，一定要先给数列排好序，因为原数组没有重叠，所以方法可行
'''