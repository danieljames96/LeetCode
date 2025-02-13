class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        start = 0
        max_length = 0

        def expand_center(left: int, right: int) -> tuple:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            
            return left+1, right - left - 1

        for i in range(len(s)):
            
            left, length = expand_center(i, i)
            if length > max_length:
                start = left
                max_length = length
            
            if i < len(s) - 1:
                left, length = expand_center(i, i+1)
                if length > max_length:
                    start = left
                    max_length = length
                
        return s[start: start + max_length]
