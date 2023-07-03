class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s = list(s)
        goal = list(goal)
        if len(s)<2:
            return False
        if len(s)!=len(goal):
            return False
        if s==goal:
            if len(set(s))>1 and len(set(s))!=len(s)//2:
                return False
            return True
        c=0
        l=[]
        for i in range(len(s)):
            if s[i] !=goal[i]:
                l.append(i)
                c+=1 
                if len(l)==2:
                    s[l[0]],s[l[1]] = s[l[1]],s[l[0]]
                    return s==goal 