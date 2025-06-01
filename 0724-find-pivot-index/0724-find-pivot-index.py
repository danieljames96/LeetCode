class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        pivot_index = 0
        left_sum = 0
        right_sum = sum(nums[pivot_index+1:])

        if left_sum == right_sum:
            return pivot_index

        pivot_index += 1

        while pivot_index < len(nums):
            
            left_sum += nums[pivot_index-1]
            right_sum -= nums[pivot_index]
            
            if left_sum == right_sum:
                return pivot_index
            
            pivot_index += 1
        
        return -1            