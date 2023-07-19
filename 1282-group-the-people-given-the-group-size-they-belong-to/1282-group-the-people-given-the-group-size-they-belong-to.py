class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if size not in dic:
                dic[size] = [i]
            else:
                dic[size].append(i)
        l = []
        for size,people in dic.items():
            for i in range(0,len(people),size):
                l.append(people[i:i+size])
        return l
