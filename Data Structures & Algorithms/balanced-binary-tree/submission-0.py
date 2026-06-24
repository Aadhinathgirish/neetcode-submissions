# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if curr is None :
                return 0
            leftheight = dfs(curr.left)
            if leftheight == -1:
                return -1
            rightheight = dfs(curr.right)
            if rightheight == -1:
                return -1
            if abs(leftheight - rightheight)>1:
                return-1
            return 1+max(leftheight,rightheight)
        return dfs(root)!=-1        
        