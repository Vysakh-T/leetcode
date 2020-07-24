class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set1 = set(i for i in range(1,len(nums)+1))
        nums = set(nums)

        return list(set1.difference(nums))