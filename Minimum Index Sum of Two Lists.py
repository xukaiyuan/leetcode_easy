class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        tmp = {}
        sum_index = len(list1) + len(list2)
        res = []

        for i in range(len(list1)):
            tmp[list1[i]] = i

        for i in range(len(list2)):
            if(list2[i] in tmp):
                sum_tmp = i + tmp[list2[i]]
                if(sum_tmp < sum_index):
                    sum_index = sum_tmp
                    res = []
                    res.append(list2[i])
                elif(sum_tmp == sum_index):
                    res.append(list2[i])
        return res