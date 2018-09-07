class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        stmp = ""
        self.backTracking(S, res, stmp, 0)
        return res

    def backTracking(self, S, res, stmp, i):
    	if(i == len(S)):
    		res.append(stmp)
    	else:
    		if(S[i].isdigit()):
    			stmp += S[i]
    			self.backTracking(S, res, stmp, i + 1)
    		else:
    			self.backTracking(S, res, stmp + S[i].upper(), i + 1)
    			self.backTracking(S, res, stmp + S[i].lower(), i + 1)