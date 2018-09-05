class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(M)
        width = len(M[0])
        res = [[0] * width for _ in range(length)]
        for i in range(length):
        	for j in range(width):
        		mask = self.mask(i, j)
        		sum_tmp = 0
        		count = 0
        		for cord in mask:
        			if(cord[0] in range(0, length) and cord[1] in range(0, width)):
        				count += 1
        				sum_tmp += M[cord[0]][cord[1]]
        		res[i][j] = math.floor(sum_tmp / count)
        return res

    
    def mask(self, i, j):
    	res = []
    	for p in range(-1, 2):
    		for q in range(-1, 2):
    			res.append([i + p, j + q])
    	return res