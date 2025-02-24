class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s[-1::-1] == s