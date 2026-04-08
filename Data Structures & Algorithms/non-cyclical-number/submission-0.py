class Solution:
    def isHappy(self, n: int) -> bool:
        seen= set()
        total=0
        while n>0:
            while n !=0:
                digit= n%10
                n= n//10
                total = total+digit*digit
            if total in seen:
                return False
            else:
                seen.add(total)
            n=total
            if total == 1:
                return True
            else:
                total=0
            