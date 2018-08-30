class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.traversal(s, t)


    def identical(self, s, t):
        if(s == None and t == None):
            return True
        if(s == None or t == None):
            return False
        return s.val == t.val and self.identical(s.left, t.left) and self.identical(s.right, t.right)

    def traversal(self, s, t):
        return (s != None) and (self.identical(s, t) or self.traversal(s.left, t) or self.traversal(s.right, t))