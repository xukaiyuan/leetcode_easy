class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        special_dict = {
            10: 'a',
            11: 'b',
            12: 'c',
            13: 'd',
            14: 'e',
            15: 'f'
        }
        
        if num < 0:
            num = 0xffffffff + num + 1
        
        rslt = []
        res = 0
        while  num >= 16:
            res = int(num%16)
            num = int(num/16)
            rslt = [special_dict.get(res, "%s" % res)] + rslt
        rslt = [special_dict.get(num, "%s" % num)] + rslt
        
        return ''.join(x for x in rslt)