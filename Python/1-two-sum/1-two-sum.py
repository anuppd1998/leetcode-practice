class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through each element in the list
        for i in range(len(nums)):
            
            # For each element, check all elements after it
            for j in range(i + 1, len(nums)):
                
                # Check if the current pair adds up to the target
                if nums[i] + nums[j] == target:
                    
                    # If found, return their indices
                    return [i, j]
