class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for indx, val in enumerate(nums):
            numMap[val] = indx
        
        for indx, val in enumerate(nums):
            complement = target - val
            if complement in numMap and numMap[complement] != indx:
                return [indx, numMap[complement]]