class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_values_in_nums = set(nums)
        longest_sequence = 0

        for num in unique_values_in_nums: 
            if (num - 1) not in unique_values_in_nums :
                length_of_current_sequence = 1
                while (num + length_of_current_sequence) in unique_values_in_nums:
                   length_of_current_sequence+=1
                longest_sequence = max(length_of_current_sequence,longest_sequence)
            else :
                continue
        return longest_sequence
            
