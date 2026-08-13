class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        matrix_lower_bound = 0
        matrix_upper_bound = len(matrix) - 1

        while matrix_lower_bound <= matrix_upper_bound : 
            middle_list = (matrix_lower_bound + matrix_upper_bound)//2

            if matrix[middle_list][0] <= target and matrix[middle_list][-1] >= target :
                return self.__searchElement( matrix[middle_list] , target)


            if matrix[middle_list][0] > target : 
                matrix_upper_bound = middle_list - 1

            if matrix[middle_list][-1] < target :
                matrix_lower_bound = middle_list + 1

        return False


    def __searchElement(self, tinyMatrix: List[int], target: int) -> bool:
        lower_bound = 0
        upper_bound = len(tinyMatrix) - 1

        while lower_bound <= upper_bound : 
            middle = (lower_bound + upper_bound)//2

            if tinyMatrix[middle] > target : 
                upper_bound = upper_bound - 1
                continue

            if tinyMatrix[middle] < target :
                lower_bound = lower_bound + 1
                continue
            
            return True

        return False

        