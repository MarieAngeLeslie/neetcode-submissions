class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsHash = {}
        for num in nums : 
            if num in numsHash :
                numsHash[num] += 1
                return True
            else :
                numsHash[num] = 1 
        return False