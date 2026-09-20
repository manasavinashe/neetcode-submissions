class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Hint 1: LeetCode only passes nums and target, so start the helper here
        return self.helper(nums, target, 0, len(nums) - 1)

    def helper(self, nums, target, l, r):
        # Hint 4: if the range is empty, the target isn't there
        if l > r:
            return -1

        mid = (r - l) // 2 + l

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            # Hints 2 & 3: return the result, and skip mid (it's already checked)
            return self.helper(nums, target, mid + 1, r)
        else:
            return self.helper(nums, target, l, mid - 1)