import collections


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        q = collections.deque()
        nodes = collections.deque()
        q.append(root)
        while len(q) != 0:
            pred = q.popleft()
            nodes.append(pred)
            while len(q) != 0:
                now = q.popleft()
                pred.next = now
                pred = now
                nodes.append(now)
            while len(nodes) != 0:
                node = nodes.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return root
