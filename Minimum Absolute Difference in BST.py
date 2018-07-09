# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    pre = None
    difference = float('inf')
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        

        if(root == None):
            return self.difference

        self.getMinimumDifference(root.left)
        
        if(self.pre != None):
            self.difference = min(self.difference, abs(root.val - self.pre))
        self.pre = root.val

        self.getMinimumDifference(root.right)

        return self.difference
        
    
