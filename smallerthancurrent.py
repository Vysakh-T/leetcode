class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for i in range(len(nums)):
            temp = 0
            for a in nums:
                if(a<nums[i]):
                    temp+=1
            r.append(temp)
        nums = r
        r = []
        return nums