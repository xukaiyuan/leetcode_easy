class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        end = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        for i in range(len(nums) - 1, -1, -1):
            if(nums[i] not in end):
                end[nums[i]] = i

        degree = 0
        num = []
        for i in count:
            if(count[i] > degree):
                num = [i]
                degree = count[i]
            elif(count[i] == degree):
                num.append(i)

        res = len(nums) + 1
        for i in num:
            tmp = end[i] - nums.index(i) + 1
            res = min(res, tmp)

        return res