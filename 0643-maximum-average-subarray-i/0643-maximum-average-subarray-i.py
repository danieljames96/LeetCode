class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        start = 0
        end = k-1
        max_sum = -float('inf')

        if k == len(nums):
            return sum(nums)/k

        while end < len(nums):
            max_sum = max(sum(nums[start:end+1]), max_sum)
            start += 1
            end += 1

        return max_sum/k