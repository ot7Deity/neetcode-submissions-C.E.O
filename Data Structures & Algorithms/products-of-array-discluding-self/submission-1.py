class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        zero=nums.count(0)
        if zero>1:
            return [0]*len(nums)
        for num in nums:
            if num !=0:
                total*=num
        output=[]
        for num in nums:
            if zero ==1:
                output.append(total if num==0 else 0)
            else:
                output.append(total//num)
        return output
        
            
        

