class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def gcd(num1, num2):
            
            for i in range(min(num1, num2), 0, -1):
                if num1 % i == 0 and num2 % i == 0:
                    return i
        
        gcd_str = ''

        if str1 + str2 == str2 + str1:
            gcd_num = gcd(len(str1), len(str2))
            # print(f'GCD: {gcd_num}')
            gcd_str = str1[:gcd_num]

        return gcd_str