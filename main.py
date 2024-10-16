from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    
    # Traverse the array once to solve the problem
    for i, num in enumerate(nums):
        complement = target - num
        
        # If the complement is in, return the result
        if complement in num_map:
            return [num_map[complement], i]
        
        # If the complement is not found
        num_map[num] = i

