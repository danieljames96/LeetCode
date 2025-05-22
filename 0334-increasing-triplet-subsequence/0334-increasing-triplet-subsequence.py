class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        out = [float(inf), float(inf), float(inf)]
        
        for i in nums:
            if i <= out[0]:
                out[0] = i
            elif i <= out[1]:
                out[1] = i
            elif i <= out[2]:
                out[2] = i

        if float(inf) in out:
            return False
        else:
            return True