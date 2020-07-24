class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x = nums[0:n]
        y = nums[n:(2*n)]
        nums = []
        for i in range(n):
            nums.append(x[i])
            nums.append(y[i])
        return nums