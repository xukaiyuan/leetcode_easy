# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        self.reversInOrder(root)
        return root

    def reversInOrder(self, root):
        if(root == None):
            return
        self.reversInOrder(root.right)
        root.val += self.sum
        self.sum = root.val
        self.reversInOrder(root.left)