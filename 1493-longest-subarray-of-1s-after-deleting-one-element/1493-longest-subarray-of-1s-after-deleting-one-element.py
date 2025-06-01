class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        if 1 not in nums:
            return 0
        
        count = 0
        zero = False
        zero_idx = -1
        max_count = 0
        for idx, num in enumerate(nums):
            if num == 0 and not zero:
                zero = True
                zero_idx = idx
                continue
            elif num == 0 and zero:
                max_count = max(count, max_count)
                # zero = False
                count = idx - zero_idx - 1
                zero_idx = idx
                # print(f'At idx {idx} New Count: {count}')
            elif idx == len(nums) - 1 and not zero:
                # print(f'Last element no zero')
                break
            else:
                count += 1
        
        max_count = max(count, max_count)

        return max_count