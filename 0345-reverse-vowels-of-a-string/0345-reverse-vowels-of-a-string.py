class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_ind = []
        new_str = []
        vowels = ['a','e','i','o','u']
        for i in range(len(s)):
            if s[i].lower() in vowels:
                vowel_ind.append(i)
            new_str.append(s[i])
            
        start = 0
        end = len(vowel_ind) - 1

        while start < end:
            new_str[vowel_ind[start]] = s[vowel_ind[end]]
            new_str[vowel_ind[end]] = s[vowel_ind[start]]
            start += 1
            end -= 1

        return ''.join(new_str)