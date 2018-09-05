class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if(root == None):
        	return False
        res = []
        self.preOrder(root, res)
        dic = {}
        for i in range(len(res)):
        	dic[k - res[i]] = i
        for i in range(len(res)):
        	if(res[i] in dic and i != dic[res[i]]):
        		return True
        return False

    def preOrder(self, root, res):
    	if(root == None):
    		return
    	self.preOrder(root.left, res)
    	res.append(root.val)
    	self.preOrder(root.right, res)