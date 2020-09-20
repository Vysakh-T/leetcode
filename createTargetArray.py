class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        target = [None for x in range(n)]
        for i in range(n):
            if target[index[i]]==None:
                target[index[i]] = nums[i]
            else:
                target = target[0:index[i]] + [nums[i]] + target[index[i]:n] 
        target = [x for x in target if x!=None]
        return target
        #Use insert() for a better solution