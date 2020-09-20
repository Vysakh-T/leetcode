class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0,len(nums),2):
            temp = [nums[i+1] for x in range(nums[i])]
            res.extend(temp)
        return res