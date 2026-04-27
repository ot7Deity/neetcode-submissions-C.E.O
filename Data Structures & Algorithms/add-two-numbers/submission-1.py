# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num=[]
        l2_num=[]
        while l1:
            l1_num.append(str(l1.val))
            l1=l1.next
        while l2:
            l2_num.append(str(l2.val))
            l2=l2.next
        solution=int("".join(l1_num[::-1]))+int("".join(l2_num[::-1]))
        dummy = ListNode(0)
        curr = dummy
        while True:
            digit=solution%10
            curr.next = ListNode(digit)
            solution=solution//10
            curr=curr.next
            if solution==0:
                break
        return dummy.next



            
            
            
