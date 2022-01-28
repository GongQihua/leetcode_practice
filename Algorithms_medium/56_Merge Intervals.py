class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        st = ed = -1
        res = []
        for s, e in intervals:
            if ed < s:
                if st != -1:
                    res.append([st, ed])
                st, ed = s, e
            else:
                ed = max(ed, e)
        if st != -1:
            res.append([st, ed])
        return res
'''
创一个上线边界，在循环list的时候挨个比较，下一个数组越过了上一个的上边界就存储，
没越过就扩展边界，在下一次循环储存
方法有两个注意点，首先要整理数组，要从小到大排列
其次是最后一次会没保存，要额外存储一下
'''