# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root]) #初始只进去了一个主节点，len=1
        while q:
            t = []
            for _ in range(len(q)):
                node = q.popleft()
                #print('node.val = ',node.val)
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                    #print('node.left.val = ',node.left.val)
                if node.right:
                    q.append(node.right)
                    #print('node.right.val = ',node.right.val)
            ans.append(t)
        return ans

'''
经典层序遍历，思路是，新建个数列，挨个放入树，每放入一个就作为节点检查左右树
这是测试输出结果：
node.val =  3
node.left.val =  9
node.right.val =  20
node.val =  9
node.val =  20
node.left.val =  15
node.right.val =  7
node.val =  15
node.val =  7
这是三次循环中q的长度，也是解法巧妙的地方：
len(q) = 1
t = [3]
len(q) = 2
t = [9, 20]
len(q) = 2
t = [15, 7]

deque的一整个部分都只是q里的一个单位，pop了就没了
'''