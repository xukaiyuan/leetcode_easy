# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt = 0
        self.postorder(root)
        return self.tilt

    def postorder(self, root):
        if(not root):
            return 0
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        self.tilt += abs(left - right)
        return left + right + root.val