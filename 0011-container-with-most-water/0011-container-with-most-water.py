class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ht = 0
        max_dt = 0
        start = 0
        last = len(height) - 1
        max_area = 0

        if len(height) < 2:
            return 0

        while start < len(height)-1 and last > start:
            ht = min(height[start], height[last])
            wt = last - start
            max_area = max(max_area, ht*wt)
            if height[start] > height[last]:
                last -= 1
            else:
                start += 1
        
        return max_area