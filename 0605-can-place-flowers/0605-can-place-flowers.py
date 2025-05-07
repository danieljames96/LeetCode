class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue

            prev = 0 if i == 0 else flowerbed[i-1]
            next = 0 if i == len(flowerbed) - 1 else flowerbed[i+1]

            if prev == 0 and next == 0:
                count += 1
                flowerbed[i] = 1
        
        if count < n:
            return False
        else:
            return True