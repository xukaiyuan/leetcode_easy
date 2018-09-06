"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        relation = {}
        for i in range(len(employees)):
            key = employees[i].id
            relation[key] = employees[i]

        queue = []
        res = 0
        queue.append(relation[id])
        

        while(len(queue) != 0):
            tmp = queue.pop(0)       
            res += tmp.importance
            subordinates = tmp.subordinates
            for i in subordinates:
                queue.append(relation[i])
        return res
