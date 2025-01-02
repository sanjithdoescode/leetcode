'''
Day - 2
Problem - 2559
Count Vowel Strings In Ranges

You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
'''
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        length = len(words)
        words_truth = [0] * (length + 1)  
        count = 0
        result = []

        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            
            words_truth[i + 1] = count  
        
        
        for query in queries:
            result.append(words_truth[query[1] + 1] - words_truth[query[0]])
        
        return result
