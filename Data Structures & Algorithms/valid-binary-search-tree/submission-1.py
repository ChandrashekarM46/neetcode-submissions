from abc import abstractproperty
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       if not root:
         return False

       from collections import deque

       q=deque([root])

       while(q):
        l=len(q)

        for _ in range(l):
            node = q.popleft()
            if node.left and node.right:
                if not node.left.val < node.val < node.right.val:
                   return False
            elif not node.left and not node.right:
                break
            else:
                return False
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
        
        return True


