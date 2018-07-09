class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if(word.islower() or word.isupper()):
            return True
        elif(word[0].isupper() and word[1:].islower()):
            return True
        else:
            return False
