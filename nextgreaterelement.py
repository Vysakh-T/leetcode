class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nge = {}
        stack = []
        for i in nums2:
            if not stack or stack[-1]>i:
                stack.append(i)
            else:
                while (stack and i>stack[-1]):
                    nge[stack.pop()]=i
                stack.append(i)
        for i in stack:
            nge[i]=-1
        stack = []
        for i in nums1:
            stack.append(nge[i])
        return stack