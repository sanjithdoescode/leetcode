'''
Day - 12
Problem - 2116
Check if a Parantheses String Can Be Valid

A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

'''


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stringLength = len(s)
        
        if stringLength % 2 == 1:
            return False

        openIndices = []
        unlockedIndices = []

        for i in range(stringLength):
            if locked[i] == '0':
                unlockedIndices.append(i)
            elif s[i] == '(':
                openIndices.append(i)
            elif s[i] == ')':
                if openIndices:
                    openIndices.pop()
                elif unlockedIndices:
                    unlockedIndices.pop()
                else:
                    return False

        while openIndices and unlockedIndices and openIndices[-1] < unlockedIndices[-1]:
            openIndices.pop()
            unlockedIndices.pop()

        if not openIndices and unlockedIndices:
            return len(unlockedIndices) % 2 == 0

        return not openIndices
