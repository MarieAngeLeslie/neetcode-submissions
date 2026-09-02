class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        final_result = 0

        while left <= right : 
            minimum_integer_k = (left + right)//2

            total_hour = 0
            for pile in piles :
                total_hour += math.ceil(pile/minimum_integer_k)
            if total_hour > h :
                left = minimum_integer_k + 1
            else : 
                final_result = minimum_integer_k
                right = minimum_integer_k - 1
        return final_result
