# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        count = {}
        self.inOrder(root, res, count)
        res.sort()
        if(len(res) <= 1):
            return -1 
        return res[1]
    
    def inOrder(self, root, res, count):
    	if(root == None):
    		return
    	self.inOrder(root.left, res, count)
    	if(root.val not in count):
    		res.append(root.val)
    		count[root.val] = 1
    	self.inOrder(root.right, res, count)