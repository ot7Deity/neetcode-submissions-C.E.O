class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for char in nums:
            seen.add(char)
        if len(seen)!=len(nums):
            return True
        else:
            return False
        
        
        