class Solution(object):
    
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lis1 = ListNode()
        lis2 = lis1
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                lis2.next = l1
                l1 = l1.next
            else:
                lis2.next = l2
                l2 = l2.next
            lis2 = lis2.next
        
        while l1 != None:
                lis2.next = l1
                l1 = l1.next
                lis2 = lis2.next
        while l2 != None:
                lis2.next = l2
                l2 = l2.next
                lis2 = lis2.next
            
        return lis1.next



