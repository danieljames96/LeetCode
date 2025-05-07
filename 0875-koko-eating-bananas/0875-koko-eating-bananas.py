import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        min_k = 1
        max_k = 10e9
        mid = min_k + (max_k - min_k)//2

        def check_feasible(k):

            count = 0
            for i in range(len(piles)):
                if piles[i] <= k:
                    count += 1
                else:
                    count += math.ceil(piles[i]/k)

            return count <= h

        while min_k < max_k:
            if check_feasible(mid):
                # print(f'Feasible for k: {mid}')
                max_k = mid
            else:
                # print(f'Not feasible for k: {mid}')
                min_k = mid+1
            mid = min_k + (max_k - min_k)//2
        
        return int(mid)
            