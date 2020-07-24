class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = None
        t = len(nums)
        i=0
        while(i<t):
            if(nums[i]==temp):
                nums.pop(i)
                t-=1
            else:
                temp = nums[i]
                i+=1
        
        return len(nums)