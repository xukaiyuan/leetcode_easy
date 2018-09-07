class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -1
        peak = max(nums)
       
        
        for i in nums:
            if(peak != i and peak < 2 * i):
                return -1
            
        return nums.index(peak)