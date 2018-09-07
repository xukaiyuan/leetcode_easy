class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if(len(J) == 0 or len(S) == 0):
        	return 0
        res = 0
        for i in S:
        	if(i in J):
        		res += 1

        return res