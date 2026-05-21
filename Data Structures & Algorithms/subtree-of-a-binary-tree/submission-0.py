# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issame(root,subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return issame(root.left,subRoot.left) and issame(root.right,subRoot.right)
        def dfs(node):
            if not node:
                return False
            return issame(node, subRoot) or dfs(node.left) or dfs(node.right)
        
        return dfs(root)