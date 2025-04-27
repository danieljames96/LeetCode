class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        if len(dp) > 1:
            dp[1] = max(nums[0], nums[1])
        if len(dp) > 2:
            dp[2] = max(nums[0] + nums[2], nums[1])

        if len(dp) > 3:
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i], dp[i-3] + nums[i])
            
        return max(dp)