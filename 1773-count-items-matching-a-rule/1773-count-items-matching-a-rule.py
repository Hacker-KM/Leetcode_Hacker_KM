class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey=="type":
            k=0
        elif ruleKey=="color":
            k=1
        elif ruleKey=="name":
            k=2
        c = 0
        for i in items:
            if i[k]==ruleValue:
                c+=1
        return c