class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = len(nums)
        i = 0
        while(i<count):
            if nums[i]==val:
                nums[i] = nums[count-1]
                count -= 1
                i-=1
            i+=1
        return count