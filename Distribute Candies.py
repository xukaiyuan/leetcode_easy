class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        res = 0
        count = {}
        for i in candies:
            if(i not in count):
                count[i] = 1
                res += 1
        return min(res, int(len(candies) / 2))
        