class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = -1*abs(nums[abs(nums[i])-1])
            
            
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
                
        return res