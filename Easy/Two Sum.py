class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dic:
                return [dic[val], i]
            dic[nums[i]] = i