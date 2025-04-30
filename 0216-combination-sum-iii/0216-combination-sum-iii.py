class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def dfs(start: int, remaining_sum: int):
            if remaining_sum == 0 and len(combination) == k:
                ans.append(combination[:])
                return
            
            if start > 9 or start > remaining_sum or len(combination) > k:
                return

            combination.append(start)
            dfs(start+1, remaining_sum-start)

            # Backtrack
            combination.pop()
            dfs(start+1, remaining_sum)
        
        combination = []
        ans = []
        
        dfs(1, n)

        return ans
                
                