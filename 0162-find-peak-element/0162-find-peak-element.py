class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        high = len(nums) - 1
        low = 0
        mid = 0

        if len(nums) == 1:
            return 0

        while low <= high:

            mid = (high + low)//2
            if mid == 0:
                ref_l = -float('inf')
                ref_h = nums[mid+1]
            elif mid == len(nums) - 1:
                ref_h = float('inf')
                ref_l = nums[mid-1]
            else:
                ref_h = nums[mid+1]
                ref_l = nums[mid-1]

            if nums[mid] > ref_l and nums[mid] > ref_h:
                return mid
            if nums[mid] < ref_h:
                low = mid+1
            else:
                high = mid-1
            
        return -1
