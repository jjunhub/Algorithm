# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
            
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
            
        if num1 == "":
            num1 = 0
        if num2 == "":
            num2 = 0
        
        res = str(int(num1) + int(num2))
        node = ListNode(res[0])
        for r in res[1:]:
            newNode = ListNode(r, node)
            node = newNode
        
        return node
        
            
            