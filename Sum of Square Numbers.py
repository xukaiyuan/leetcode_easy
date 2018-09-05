class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(math.sqrt(c)) + 1):
        	b = c - a ** 2
        	if(math.sqrt(b) - math.floor(math.sqrt(b)) == 0):
        		return True
        return False