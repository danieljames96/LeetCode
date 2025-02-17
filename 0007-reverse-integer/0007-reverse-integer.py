class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = '-'
        else:
            sign = ''

        num = str(abs(x))
        newNum = ''
        
        for i in range(len(num)-1, -1, -1):
            newNum += num[i]
        
        if x < 0 and int(newNum) > (2 ** 31):
            return 0
        if x > 0 and int(newNum) > (2 ** 31) - 1:
            return 0

        return int(sign + newNum)