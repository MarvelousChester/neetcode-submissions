class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a unique only list, if trying to add and that value exists, welp we found dupe
        seen = set()
        for num in nums:
            if num in seen:
                return True  # Early exit as soon as a duplicate is found
            seen.add(num)
        return False
