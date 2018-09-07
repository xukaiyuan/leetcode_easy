class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        res = []
        for i in range(left, right + 1):
            if(i < 10):
                res.append(i)
            else:
                res.append(i)
                tmp = str(i)
                if("0" not in tmp):
                    for j in tmp:
                        if(i % int(j) != 0):
                            res.pop()
                            break
                else:
                    res.pop()
                    
        return res

