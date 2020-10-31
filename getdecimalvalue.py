# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = []
        ans = 0
        while(head!=None):
            res.append(head.val)
            head = head.next
        for i,s in enumerate(res[::-1]):
            ans += s*(2**i)
        return ans

#Use bit manipulation for better runtime and memory usage