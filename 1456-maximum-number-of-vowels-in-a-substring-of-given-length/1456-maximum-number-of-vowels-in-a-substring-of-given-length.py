class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ['a','e','i','o','u']

        if k == len(s):
            return sum([1 for ch in s if ch in vowels])
        
        start = 0
        end = start + k - 1

        vowel_count = sum([1 for ch in s[start:end+1] if ch in vowels])
        max_vowels = vowel_count
        # print(f'Initial vowel_count: {vowel_count} for substring: {s[start:end+1]}')

        start += 1
        end += 1

        while end < len(s):
            left = 1 if s[start-1] in vowels else 0
            right = 1 if s[end] in vowels else 0
            vowel_count = vowel_count - left + right
            max_vowels = max(max_vowels, vowel_count)
            # print(f'Vowel Count is {vowel_count} for substring {s[start:end+1]}')
            start += 1
            end += 1
        
        return max_vowels