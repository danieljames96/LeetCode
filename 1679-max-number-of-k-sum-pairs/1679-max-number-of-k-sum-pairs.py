class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        removed = []
        count = 0

        for i in range(len(nums)-1):
            if i in removed:
                continue
            for j in range(i+1, len(nums)):
                if j in removed:
                    continue

                if nums[i] + nums[j] == k:
                    count += 1
                    removed.extend([i, j])
                    break
        
        return count