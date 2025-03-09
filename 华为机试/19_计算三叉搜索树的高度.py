import sys

class Node:
    def __init__(self, v):
        self.val = v
        self.mid = None
        self.left = None
        self.right = None

def create(node, v):
    if node == None:
        return Node(v)
    if node.val - 500 > v:
        node.left = create(node.left, v)
    elif node.val + 500 < v:
        node.right = create(node.right, v)
    else:
        node.mid = create(node.mid, v)
    return node

def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right), height(root.mid)) + 1

def main():
    N = int(input())
    q = []
    for line in sys.stdin:
        for x in line.split(" "):
            q.append(int(x))
    
    root = Node(q[0])
    for i in range(1, len(q)):
        create(root, q[i])
    
    print(height(root))

if __name__ == "__main__":
    main()