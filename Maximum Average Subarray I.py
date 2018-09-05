class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = 0
        for i in range(k):
        	sum += nums[i]

        res = sum
        for i in range(k, len(nums)):
        	sum += nums[i] - nums[i - k]
        	res = max(sum, res)
        return res / k