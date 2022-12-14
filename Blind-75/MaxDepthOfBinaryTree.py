# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #base case
        if not root:
            return 0
        #break the problem into sub problems. We want to keep exploring right and
        #left subtrees for every set of three nodes, if null, return 0 as in the base case
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
            
