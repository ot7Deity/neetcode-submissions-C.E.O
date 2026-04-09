class Solution:
    def isValid(self, s: str) -> bool:
        compliment={"]":"[",")":"(","}":"{"}
        stack=[]

        for char in s:
            if char not in compliment:
                stack.append(char)
            elif not stack or compliment[char]!=stack[-1]:
                return False
            elif compliment[char]==stack[-1] :
                stack.pop()

        return len(stack)==0


        