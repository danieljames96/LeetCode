class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        current_substr = ''
        longest_substr = ''
        for c in s:
            print('c: '+c)
            print('current_substr: '+current_substr)
            print('longest_substr: '+longest_substr)
            index = current_substr.find(c)
            if index == -1:
                current_substr += c
            else:
                if len(current_substr) > len(longest_substr):
                    longest_substr = current_substr
                current_substr = current_substr[index+1:] + c
        
        if len(current_substr) > len(longest_substr):
            longest_substr = current_substr

        return len(longest_substr)
