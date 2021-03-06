class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if(len(flowerbed) == 1):
            return flowerbed[0] == 0 or n == 0
        for i in range(len(flowerbed)):
            if(n == 0):
                return True
            if(i == 0):
                if(flowerbed[i] == 0 and flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
            if(i == len(flowerbed) - 1):
                if(flowerbed[i - 1] == 0 and flowerbed[i] == 0):
                    flowerbed[i] = 1
                    n -= 1

            else:
                if(flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1

        return n == 0