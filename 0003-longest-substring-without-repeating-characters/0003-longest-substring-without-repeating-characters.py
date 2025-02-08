class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_position = {}
        max_length = 0
        start = 0

        for end, char in enumerate(s):
            if char in char_position and char_position[char] >= start:
                start = char_position[char] + 1
            else:
                max_length = max(max_length, end - start + 1)
            
            char_position[char] = end

        return max_length
