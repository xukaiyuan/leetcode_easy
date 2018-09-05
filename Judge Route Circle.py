class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        if(len(moves) == 0 or len(moves) == 1):
            return False

        for i in moves:
            if(i == "U"):
                y += 1
            elif(i == "D"):
                y -= 1
            elif(i == "L"):
                x -= 1
            else:
                x += 1
        if(x == 0 and y == 0):
            return True
        return False