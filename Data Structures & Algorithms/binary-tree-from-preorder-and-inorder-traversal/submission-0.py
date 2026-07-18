# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i,k in enumerate(inorder):
            hashmap[k] = i
        def bulid(prestart,preend,istart,iend):
            if prestart > preend:
                return None
            root = TreeNode(preorder[prestart])
            index = hashmap[preorder[prestart]]
            leftsize = index - istart
            root.left = bulid(prestart+1,prestart+leftsize,istart,index-1)
            root.right = bulid(prestart+leftsize+1,preend,index+1,iend)
            return root
        return bulid(0,len(preorder)-1,0,len(inorder)-1)

