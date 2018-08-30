class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if(len(nums) == 0 or r * c != len(nums) * len(nums[0])):
            return nums
        tmp = []

        for i in range(len(nums)):
            for j in range(len(nums[0])):
                tmp.append(nums[i][j])
        
        res = [([0] * c) for _ in range(r)]
        for i in range(r):
            for j in range(c): 
                res[i][j] = tmp.pop(0)
                
        return res