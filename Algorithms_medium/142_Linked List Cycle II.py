# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        has_cycle = False
        while not has_cycle and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            has_cycle = slow == fast
        if not has_cycle:
            return None
        p = head
        while p != slow:
            p, slow = p.next, slow.next
        return p

'''
这题写起来没难度，主要是思路，这里放上官方的解法，其实重点就是怎么找那个循环的点
先利用快慢指针判断链表是否有环，没有环则直接返回 null。
若链表有环，我们分析快慢相遇时走过的距离。
对于慢指针（每次走 1 步），走过的距离为 S=X+Y ①；快指针（每次走 2 步）走过的距离为 2S=X+Y+N(Y+Z) ②。
如下图所示，其中 N 表示快指针与慢指针相遇时在环中所走过的圈数，而我们要求的环入口，也即是 X 的距离：
我们根据式子 ①②，得出 X+Y=N(Y+Z) => X=(N-1)(Y+Z)+Z。
当 N=1(快指针在环中走了一圈与慢指针相遇) 时，X=(1-1)(Y+Z)+Z，即 X=Z。此时只要定义一个 p 指针指向头节点，然后慢指针与 p 开始同时走，当慢指针与 p 相遇时，也就到达了环入口，直接返回 p 即可。
当 N>1时，也是同样的，说明慢指针除了走 Z 步，还需要绕 N-1 圈才能与 p 相遇。
'''