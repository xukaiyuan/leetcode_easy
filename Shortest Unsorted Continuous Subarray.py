class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        stack = []
        lindex = len(nums)
        rindex = 0
        for i in range(len(nums)):
            while(len(stack) != 0 and nums[i] < nums[stack[-1]]):
                tmp = stack.pop()
                lindex = min(lindex, tmp)
            stack.append(i)

        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while(len(stack) != 0 and nums[i] > nums[stack[-1]]):
                tmp = stack.pop()
                rindex = max(rindex, tmp)
            stack.append(i)
        
        if(rindex > lindex):
            return rindex - lindex + 1
        else:
            return 0
