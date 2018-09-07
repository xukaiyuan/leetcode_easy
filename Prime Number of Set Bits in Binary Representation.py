class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        res = 0
        for i in range(L, R + 1):
        	count = self.count(i)
        	if(count in prime):
        		res += 1
        return res
    
    
    def count(self, num):
    	count = 0
    	while(num != 0):
    		count += num & 1
    		num >>= 1
    	return count