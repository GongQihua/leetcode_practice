# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda a, b: a.val < b.val) #设置属性
        pq = [head for head in lists if head]
        heapify(pq) #将heap属性强制应用到任意一个列表
        dummy = cur = ListNode()
        while pq:
            node = heappop(pq) #将数组堆中的最小元素弹出
            if node.next:
                heappush(pq, node.next) #数据堆入
            cur.next = node
            cur = cur.next
        return dummy.next
'''
我们可以创建一个小根堆pq来维护所有链表的头节点，每次从小根堆中取出值最小的节点，
添加到结果链表的末尾，然后将该节点的下一个节点加入堆中，重复上述步骤直到堆为空。
'''