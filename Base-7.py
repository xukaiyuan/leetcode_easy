class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if(num == 0):
            return '0'
        res = ''
        tmp = abs(num)
        while(tmp / 7 != 0):
            res = str(tmp % 7) + res
            tmp = int(tmp / 7)
        if(num < 0):
            return '-' + res
        else:
            return res