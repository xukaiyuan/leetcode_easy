class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = None
        while(n != 0):
            tmp = n & 1
            if(tmp == count):
                return False
            count = tmp
            n >>= 1
        return True
        