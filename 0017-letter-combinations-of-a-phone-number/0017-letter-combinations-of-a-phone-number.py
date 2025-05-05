class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digits_to_chars = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        ans = ['']

        for digit in digits:
            s = digits_to_chars[int(digit)-2]
            ans = [a + b for a in ans for b in s]
        
        return ans