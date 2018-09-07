class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        distance = 27
        res = ""

        for i in letters:
        	tmp = ord(i) - ord(target)
        	if(tmp <= 0):
        		tmp = tmp + 26
            
        	if(tmp < distance):
        		distance = tmp
        		res = i
        return res