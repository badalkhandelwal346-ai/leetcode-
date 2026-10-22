# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        arr=[]
        def f(root):
            if root==None:
                return 
            # arr.append(root.val)
            arr.append(root.val)
            
            f(root.left)
            f(root.right)
        f(root)    
            
        return arr        
        