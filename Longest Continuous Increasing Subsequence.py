class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if(length == 0):
        	return 0
        res = 0
        start = 0
        for i in range(1, length):
        	if(nums[i] <= nums[i - 1]):
        		res = max(res, i - start)
        		start = i
        res = max(res, length - start)
        return res


