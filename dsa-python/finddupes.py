class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1