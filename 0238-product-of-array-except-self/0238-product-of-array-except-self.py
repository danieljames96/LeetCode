class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        prefixs = []
        suffixs = []
        output = []

        for i in range(len(nums)):
            prefixs.append(prefix)
            suffixs.append(suffix)
            prefix *= nums[i]
            suffix *= nums[-i-1]

        for i in range(len(nums)):
            output.append(prefixs[i] * suffixs[-i-1])
        
        return output