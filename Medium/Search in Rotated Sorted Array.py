class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        if j < 0:
            return -1
        if j == 0:
            if target == nums[j]:
                return 0
            else:
                return -1
        if target < nums[0]:
            while j >= 0 and target < nums[j]:
                j -= 1
            if j >= 0 and target == nums[j]:
                return j
            else:
                return -1
        while i < len(nums) and target > nums[i]:
            i += 1
        if i < len(nums) and target == nums[i]:
            return i
        else:
            return -1
        