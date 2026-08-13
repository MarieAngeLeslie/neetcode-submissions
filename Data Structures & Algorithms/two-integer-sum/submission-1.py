class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}
        for index, num in enumerate(nums) :
            difference = target - num
            if difference in hashNums :
                return [hashNums[difference], index]
            else : 
                hashNums[num] = index