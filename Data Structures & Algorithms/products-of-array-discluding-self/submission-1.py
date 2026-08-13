#Solution 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array_length = len(nums)
        prefix = [0] * array_length
        postfix = [0] * array_length
        result = [0] * array_length

        prefix[0] = postfix[array_length - 1] = 1

        for i in range(1, array_length) :
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(array_length-2, -1, -1) :
            postfix[i] = nums[i+1] * postfix[i+1]

        for i in range(array_length) :
            result [i] = prefix[i] * postfix[i]
           
        return result
