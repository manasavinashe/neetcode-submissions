import random

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        def partition(left, right):
            r = random.randint(left, right)
            nums[r], nums[right] = nums[right], nums[r]
            pivot = nums[right]
            i = left
            for j in range(left, right):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i

        def quicksort(left, right):
            if left >= right:
                return
            p = partition(left, right)
            quicksort(left, p - 1)
            quicksort(p + 1, right)

        quicksort(0, len(nums) - 1)