class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        length = len(matrix)
        width = len(matrix[0])
        
        for i in range(1, length):
        	for j in range(1, width):
        		if(matrix[i][j] != matrix[i - 1][j - 1]):
        			return False
        return True
