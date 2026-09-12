class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Target trouvé
            if nums[mid] == target:
                return mid

            # La moitié gauche est triée
            if nums[left] <= nums[mid]:
                # Le target peut-il être dans cette moitié ?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Sinon, la moitié droite est triée
            else:
                # Le target peut-il être dans cette moitié ?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1