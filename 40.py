'''
Day - 6
Problem - 40
Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
'''
class Solution:
    def combinationSum2(self, cand, target):
        cand.sort()
        res = []
        path = []
        self.dfs(cand, 0, target, path, res)
        return res
    
    def dfs(self, cand, cur, target, path, res):
        if target == 0:
            res.append(path.copy())
            return
        if target < 0:
            return
        
        for i in range(cur, len(cand)):
            if i > cur and cand[i] == cand[i - 1]:  # Skip duplicates
                continue
            path.append(cand[i])
            self.dfs(cand, i + 1, target - cand[i], path, res)
            path.pop()  # Backtrack
        
