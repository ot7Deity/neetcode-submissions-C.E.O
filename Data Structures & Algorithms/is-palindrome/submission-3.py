class Solution:
    def isPalindrome(self, s: str) -> bool:
        #left pointer starts at index 0
        l=0
        # right pointer starts at the end
        r= len(s)-1
        while l<=r:
            if s[l].isalnum() and s[r].isalnum():
                 # compare pointers to see if they are the same element
                if s[l].lower()==s[r].lower(): #checks if l and r are equal characters
                    l+=1 # if they are incrument left plus 1
                    r-=1 # if they are incrument right minus 1
                else:
                    return False #return false becuase we know it is not a palidrome
            else:
                if not s[l].isalnum(): # refers back to my first if statment to check if bot l and r are characters if not go to the next
                    l+=1
                if not s[r].isalnum():
                    r-=1
        return True # return true because once l and r equal each other then we know it is a palidrome
        # time complexity o(n) just goes through the string once
        # space complexity o(N) none of our variables are growing
