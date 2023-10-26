class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        def count_trees(num, arr, memo):
            if num in memo:
                return memo[num]
            
            count = 0
            for smaller_num in arr:
                if num % smaller_num == 0:
                    complement = num // smaller_num
                    if complement in arr:
                        count += count_trees(smaller_num, arr, memo) * count_trees(complement, arr, memo)
            
            memo[num] = count + 1
            return count + 1

        arr.sort()
        total_trees = 0
        memo = {} 
        for num in arr:
            total_trees += count_trees(num, set(arr), memo)
        
        return total_trees % (10**9 + 7)
