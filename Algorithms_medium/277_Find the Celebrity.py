# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        ans = 0
        for i in range(1, n):
            if knows(ans, i):
                ans = i
        for i in range(n):
            if ans != i:
                if knows(ans, i) or not knows(i, ans):
                    return -1
        return ans
'''
这里 ans认识 3，说明 i不是名人（即  0不是名人），那么名人会是  1或者 2 吗？不会！因为若 1 或者 2 是名人，那么 0 应该认识 1 或者 2 才对，与前面的例子冲突。因此，我们可以直接将 ans 更新为 3。
我们找出 ans 之后，接下来再遍历一遍，判断 ans 是否满足名人的条件。若不满足，返回 -1。
否则遍历结束，返回 。
'''