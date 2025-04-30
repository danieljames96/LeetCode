class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            check = nums.pop()
            if check in ans:
                ans.remove(check)
            else:
                ans.append(check)
        
        return ans[0]