class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def removeDuplicates(self):
        unique_nums = []
        
        for num in self.nums:
            if num not in unique_nums:
                unique_nums.append(num)
        unique_length = len(unique_nums)
        
        for i in range(len(self.nums) - len(unique_nums)):
            unique_nums.append('_')

        return unique_length, unique_nums