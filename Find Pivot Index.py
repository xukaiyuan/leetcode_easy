class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0 or len(nums) == 2):
        	return -1
        if(len(nums) == 1):
        	return 0
        total = sum(nums)
        
        tmp = 0
        index = 1

        for i in range(0, len(nums)):
        	tmp_sum = total - nums[i]
        	if(tmp == tmp_sum / 2):
        		return i
        	tmp += nums[i]
        return -1

