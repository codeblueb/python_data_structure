
from type import Optional

class TreeNode:
    def __init__(self, value = 0, left=None, right=None) -> None:
        self.value =value
        self.left = left
        self.right = right

class Solution:
    def binarytree_prune(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        def contains_one(node):
            if not root: return False
            contains_left = contains_one(node.left)
            contains_right = contains_one(node.right)
            if not contains_left:
                node.left = None
            if not contains_right:
                node.right = None
            return node.value == 1 or contains_left or contains_right
        return root if contains_one(root) else None
