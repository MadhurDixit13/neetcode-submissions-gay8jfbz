# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        def good(node, max):
            if(node !=None):
                if(node.val>=max):
                    return 1 + good(node.left, node.val) + good(node.right, node.val)
                return good(node.left,max) + good(node.right, max)
            else: 
                return 0
        return 1 + good(root.left, root.val) + good(root.right, root.val)