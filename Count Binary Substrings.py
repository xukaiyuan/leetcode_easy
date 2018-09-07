class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        group = [1]
        length = len(s)
        for i in range(1, length):
        	if(s[i] == s[i - 1]):
        		group[-1] += 1
        	else:
        		group.append(1)
        res = 0
        for i in range(len(group) - 1):
        	res += min(group[i], group[i + 1])

       	return res