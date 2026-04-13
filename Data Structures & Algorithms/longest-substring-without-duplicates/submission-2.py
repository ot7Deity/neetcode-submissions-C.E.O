class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        seen={}
        longest_len=0
        for r in range(len(s)):
            if s[r] in seen and seen[s[r]]>=l:
                l=seen[s[r]]+1
            longest_len=max(longest_len, (r-l)+1)
            seen[s[r]]=r
        return longest_len


