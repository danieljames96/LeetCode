class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        num_hash = {}
        removed = []
        count = 0

        for i in range(len(nums)):
            if num_hash.get(nums[i], 0) == 0:
                num_hash[nums[i]] = 1
            else:
                num_hash[nums[i]] += 1
        
        # print(f'num_hash: {num_hash}')

        for key, value in num_hash.items():
            if key in removed:
                continue
            
            if k-key == key:
                count += value//2
            elif num_hash.get(k-key, 0) == 0:
                continue
            else:
                count += min(value, num_hash.get(k-key, 0))
                removed.append(k-key)

        return count