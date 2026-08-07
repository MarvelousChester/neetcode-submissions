class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a unique only list, if trying to add and that value exists, welp we found dupe
        unique_nums = set(nums)
        if len(unique_nums) == len(nums):
            return False
        else:
            return True
