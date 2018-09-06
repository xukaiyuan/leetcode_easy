class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        sum = 0
        valid = []
        for i in ops:
            if(i == "C"):
                tmp = valid.pop()
                sum -= tmp
            elif(i == "+"):
                tmp = valid[-1] + valid[-2]
                valid.append(tmp)
                sum += tmp
            elif(i == 'D'):
                tmp = 2 * valid[-1]
                valid.append(tmp)
                sum += tmp
            else:
                sum += int(i)
                valid.append(int(i))
        return sum