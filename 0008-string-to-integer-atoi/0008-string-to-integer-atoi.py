class Solution:
    def myAtoi(self, s: str) -> int:
        
        num = 0
        sign = 1
        s = s.strip()

        for i in range(len(s)):
            if i == 0:
                if s[i] == '+':
                    continue
                if s[i] == '-':
                    sign = -1
                    continue
            if s[i].isdigit():
                num = num*10 + int(s[i])
            else:
                break
        
        if sign == 1 and num > (2**31) - 1:
            num = (2**31) - 1
        elif sign == -1 and num > (2**31):
            num = (2**31)

        return sign*num