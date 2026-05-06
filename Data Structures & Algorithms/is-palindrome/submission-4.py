class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower()
        stack=[]
        for char in s1:
            if char.isalnum()== False:
                continue
            stack.append(char)
            print(stack[-1])
        for char in s1:
            if char.isalnum()== False:
                continue
            if char != stack[-1]:
                return False
            print(char)
            stack.pop()
        return True
            
        