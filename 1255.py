'''
Day - 6
Problem - 1255
Maximum Score Words Formed by Letters

Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
'''

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        count = [0] * 26
        letters_count = [0] * 26
        
        for c in letters:
            count[ord(c) - ord('a')] += 1
        
        self.ans = 0
        self.backtracking(words, score, count, letters_count, 0, 0)
        return self.ans
    
    def backtracking(self, words, score, count, letters_count, pos, temp):
        for i in range(26):
            if letters_count[i] > count[i]:
                return
        
        self.ans = max(self.ans, temp)
        
        for i in range(pos, len(words)):
            for c in words[i]:
                letters_count[ord(c) - ord('a')] += 1
                temp += score[ord(c) - ord('a')]
            
            self.backtracking(words, score, count, letters_count, i + 1, temp)
            
            for c in words[i]:
                letters_count[ord(c) - ord('a')] -= 1
                temp -= score[ord(c) - ord('a')]
