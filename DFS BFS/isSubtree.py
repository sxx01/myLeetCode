# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEqual(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val != subRoot.val:
            return False
        return self.isEqual(root.left, subRoot.left) and self.isEqual(root.right, subRoot.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if root.val != subRoot.val:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            if self.isEqual(root, subRoot):
                return True
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == "__main__":
    root: TreeNode = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    subRoot: TreeNode = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    so = Solution()
    print(so.isSubtree(root, subRoot))
