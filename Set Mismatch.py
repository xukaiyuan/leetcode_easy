class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        gap = int((1 + length) * length / 2 - sum(nums))
        count = {}
        dup = -1
        for i in nums:
        	if(i in count):
        		dup = i
        		break
        	else:
        		count[i] = 1
        return [dup, dup + gap]