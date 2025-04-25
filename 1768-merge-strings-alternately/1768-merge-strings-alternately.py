class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        total_length = len1 + len2

        ind1 = 0
        ind2 = 0
        out = ''

        for ind in range(total_length):
            if ind1 < len(word1):
                out += word1[ind1]
                ind1 += 1
            if ind2 < len(word2):
                out += word2[ind2]
                ind2 += 1
        
        return out