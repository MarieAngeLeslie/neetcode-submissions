class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == h : 
            piles.sort()
            return piles[-1]
        
        if sum(piles) == h : 
            return 1
        
        
        left_pointer, rigth_pointer = 1, max(piles)
        best_result = rigth_pointer

        while left_pointer <= rigth_pointer :

            totalHours = 0

            possible_min_average = left_pointer + ( rigth_pointer - left_pointer ) // 2
            
            for i in range(len(piles)) :
                totalHours += math.ceil(piles[i] / possible_min_average)

            if  totalHours <= h : 
                best_result = possible_min_average
                rigth_pointer = possible_min_average - 1
            else: 
                left_pointer = possible_min_average + 1

        return best_result
