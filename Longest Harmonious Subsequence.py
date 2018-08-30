class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        res = 0
        tmp = 0
        for i in count:
            tmp = count[i]
            if((i + 1) in count):
                tmp += count[i + 1]
                res = max(tmp, res)

        return res