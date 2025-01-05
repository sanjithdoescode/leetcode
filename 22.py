'''
Day - 5
Problem - 22
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def rec(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                rec(left + 1, right, s  + '(')
            if right < left:
                rec(left, right + 1, s + ')')
            
        res = []
        rec(0, 0, '')
        return res
