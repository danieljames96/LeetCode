class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+1):
            num = i
            count = 0
            while num != 0:
                if num%2 == 1:
                    count += 1
                num = num // 2

            # num = format(i, 'b')
            # count = 0
            # for ch in num:
            #     if ch == '1':
            #         count+=1
            
            ans.append(count)
        
        return ans