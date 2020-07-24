class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        count = 1
        while (j<len(nums)):
            if(count==len(nums)):
                return
            if nums[j]==0:
                nums.pop(j)
                nums.append(0)
                j-=1
            j+=1
            count+=1