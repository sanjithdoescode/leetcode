'''
Day - 7
Problem - 47
Permutation II
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        visited = [False] * n
        def dfs(path, i):
            if i == n:
                res.append(path[:])
                return
            for j in range(n):
                if visited[j]: continue
                if j > 0 and nums[j] == nums[j-1] and not visited[j-1]:
                    continue
                path.append(nums[j])
                visited[j] = True
                dfs(path, i+1)
                path.pop()
                visited[j] = False
        
        dfs([], 0)
        return res
