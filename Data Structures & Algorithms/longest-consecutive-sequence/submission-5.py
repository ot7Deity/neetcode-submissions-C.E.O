class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """nums.sort()
        res=1
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                res+=1
        return res
        """
        longest=0
        numset=set(nums)
        for n in nums:
            if n-1 not in numset:
                length=0
                while n+length in numset:
                    length+=1
                longest=max(length,longest)
        return longest
        
        
