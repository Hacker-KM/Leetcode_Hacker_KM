class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Simple Brute Force Approach that passes 34 test cases and then TLE

        # if 'Y' not in customers:
        #     return 0
        # if 'N' not in customers:
        #     return len(customers)
        # l = []
        # j = len(customers) - 1
        # for i in range(len(customers)):
        #     penalty = customers[0:i].count('N') + customers[i:j+1].count('Y')
        #     l.append(penalty)
        # l.append(customers.count('N'))
        # return l.index(min(l))
        

        # ******optimised Approach*****

        penalty = customers.count('Y')
        m_penalty = penalty
        hour = 0

        for i in range(len(customers)):
            if customers[i]=='Y':
                penalty-=1
            else:
                penalty+=1
            if penalty<m_penalty:
                hour = i+1
                m_penalty = penalty
        return hour
