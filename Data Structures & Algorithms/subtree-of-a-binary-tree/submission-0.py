# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(nodeA, nodeB):
            if not nodeA and not nodeB:
                return True
            elif not nodeA or not nodeB:
                return False

            if nodeA.val != nodeB.val:
                 return False
            
            return (
                dfs(nodeA.left, nodeB.left) and
                dfs(nodeA.right, nodeB.right)
            )

        if not root:
            return False
        
        if dfs(root, subRoot):
            return True
        
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
        
        
