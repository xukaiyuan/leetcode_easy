class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_abs = 0
        late = 0

        for i in s:
            if(i == "L"):
                late += 1
                if(late == 3):
                    return False
            elif(i == "A"):
                count_abs += 1
                late = 0
                if(count_abs == 2):
                    return False
            else:
                late = 0
        return True
