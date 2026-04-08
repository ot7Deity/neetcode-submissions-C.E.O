class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if nums[i] in comp:
                return [comp[nums[i]], i]
            if compliment not in comp:
                comp[compliment]=i
           
        
            

            

        
        