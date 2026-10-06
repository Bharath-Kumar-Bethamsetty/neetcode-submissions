# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []
        def preOrder(node):
            if not node:
                return
            heapq.heappush(self.heap, node.val)
            preOrder(node.left)
            preOrder(node.right)
        
        preOrder(root)
        ans = 0
        for _ in range(k):
            ans = heapq.heappop(self.heap)
        return ans


