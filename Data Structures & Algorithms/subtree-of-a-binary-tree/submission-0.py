# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(cur1,cur2):
            if not cur1 and not cur2:
                return True
            elif not cur1 or not cur2:
                return False
            elif cur1.val!=cur2.val:
                return False
            return (sameTree(cur1.left,cur2.left) and sameTree(cur1.right,cur2.right))

        if not subRoot:
            return True
        if not root:
            return False
        if sameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))

        

            
        