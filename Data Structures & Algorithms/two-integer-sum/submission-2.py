# Notes: 
# Given an array, identify the numbers that satisfy the target
# Given [3,4,5, 6] with target 7 means I 0 and 1 are my indexes aka 3 + 4
# Core Constraint: One Valid Only Exists so can Exit after two indices that equal target 


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {num: i for i, num in enumerate(nums)}
        # loop through list
        # keep track of indice 
        # if indice - target has number within table? 
            # Yes, there where is left over number indice
            # Return pair (indice, left overn number indice)
            # IF negative, then 
        
        for count in range(len(nums)):
            num_to_check = target - nums[count]
            print(num_to_check)
            if num_to_check in table:
                if table[num_to_check] == count:
                    continue 
                return [count, table[num_to_check]]

                

        