# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def helper(root):
            if(root == None):
                return 0
            left = helper(root.left)
            right = helper(root.right)

            left_path = right_path = 0

            if(root.left and root.left.val == root.val):
                left_path = left + 1
            if(root.right and root.right.val == root.val):
                right_path = right + 1
            self. res = max(self.res, left_path + right_path)

            return max(left_path, right_path)

        helper(root)
        return self.res

