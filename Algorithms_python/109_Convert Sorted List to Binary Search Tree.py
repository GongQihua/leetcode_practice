# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def buildBST(nums, start, end):
            if start > end:
                return None
            mid = (start + end) >> 1
            return TreeNode(nums[mid], buildBST(nums, start, mid-1), buildBST(nums, mid+1, end))
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return buildBST(nums, 0, len(nums) - 1)

'''
思路是先把链表导入成一个普通的数列，然后根据数列，类似于二分法找中间数，在将中间数挨个定义为树节点
注意区分左右树就行，第一个def里的那句return那样。
'''