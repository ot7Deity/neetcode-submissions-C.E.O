class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_len=0
        if len(heights)==2:
            return min(heights)
        while l<r:
            max_len=max(max_len, (r-l)*min(heights[l],heights[r]))
            if heights[r]<heights[l]:
                r-=1
            elif heights[r]<heights[l]:
                l+=1
            else:
                l+=1
        return max_len
        