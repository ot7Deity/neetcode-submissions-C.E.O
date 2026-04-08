class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        if len(s)!=len(t):
            return False
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        for char in t:
            if char in freq:
                freq[char]-=1
            else:
                return False
        return all(x == 0 for x in freq.values())
            