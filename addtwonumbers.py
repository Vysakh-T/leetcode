# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        i = 0
        s = l1.val + l2.val
        if s>=10:
            i = 1
            s = s-10
        l3 = ListNode(s)
        l4 = l3
        
        while(l1.next != None and l2.next != None):
            l1 = l1.next
            l2 = l2.next
            s = l1.val+l2.val+i
            i = 0
            if s>=10:
                i = 1
                s = s-10
            l3.next = ListNode(s)
            l3 = l3.next
            
        
        l1 = l1 if l1.next!=None else l2
            
        while(l1.next!=None):
            l1 = l1.next
            s = l1.val+i
            if s>=10:
                i = 1
                s = s-10
            else:
                i = 0
            l3.next = ListNode(s)
            l3 = l3.next
            
        
        if i==1:
            l3.next = ListNode(i)
        return l4