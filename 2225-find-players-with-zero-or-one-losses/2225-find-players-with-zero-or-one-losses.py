class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_set = set()
        lose_set = set()
        losers = []
        
        for winner, loser in matches:
            win_set.add(winner)
            lose_set.add(loser)
            losers.append(loser)
        
        unique_losers = []
        ans = [[], []]
        c = Counter(losers)
        for loser in lose_set:
            if loser in win_set:
                win_set.remove(loser)
            if c[loser]==1:
                unique_losers.append(loser)
        
        ans[0] = sorted(list(win_set))
        ans[1] = sorted(list(unique_losers))
        
        return ans
