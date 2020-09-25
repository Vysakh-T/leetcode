class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod = max(nums)
        nums[nums.index(prod)] = -1
        prod = (prod-1)*(max(nums)-1)
        return prod