# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return(0,0)
            leftrob,leftnotrob = dfs(root.left)
            rightrob,rightnotrob = dfs(root.right)
            rob = root.val + leftnotrob + rightnotrob
            notrob = max(leftrob,leftnotrob)+max(rightrob,rightnotrob)
            return rob,notrob
        return max(dfs(root))