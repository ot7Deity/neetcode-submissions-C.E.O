class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        if len(nums)<k:
            return False
        for char in nums:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        finalv=freq.items()
        finalv=sorted(finalv, key=lambda x:x[1], reverse=True)
        for i in range(k):
            res.append(finalv[i][0])
        return res
        