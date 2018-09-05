# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        queue = []
        if(root == None):
        	return res
        queue.append(root)

        while(len(queue) != 0):
        	tmp_len = len(queue)
        	tmp_sum = 0
        	for i in range(tmp_len):
        		tmp = queue.pop(0)
        		tmp_sum += tmp.val
        		if(tmp.left != None):
        			queue.append(tmp.left)
        		if(tmp.right != None):
        			queue.append(tmp.right)
        	res.append(tmp_sum / tmp_len)
        return res
